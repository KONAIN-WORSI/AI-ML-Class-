import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os

# Global variables
original_image = None
display_image = None
mask = None
result_image = None
drawing = False
brush_size = 20
scale_factor = 1.0
last_x = 0
last_y = 0

# GUI components (will be initialized later)
root = None
canvas = None
result_canvas = None
status_var = None
brush_scale = None
brush_label = None
algorithm_var = None

def update_brush_size(value):
    """Update brush size and label"""
    global brush_size
    brush_size = int(value)
    brush_label.config(text=f"{brush_size}px")

def load_image():
    """Load an image file and prepare for editing"""
    global original_image, display_image, mask, scale_factor
    
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif"),
            ("All files", "*.*")
        ]
    )
    
    if not file_path:
        return
    
    try:
        # Load image with OpenCV
        original_image = cv2.imread(file_path)
        if original_image is None:
            raise ValueError("Could not load image")
        
        # Convert BGR to RGB for display
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        
        # Calculate scale factor for display
        canvas_width = 400  # Target display width
        canvas_height = 400  # Target display height
        
        h, w = original_image.shape[:2]
        scale_factor = min(canvas_width/w, canvas_height/h)
        
        # Resize for display
        display_w = int(w * scale_factor)
        display_h = int(h * scale_factor)
        display_image = cv2.resize(original_image, (display_w, display_h))
        
        # Initialize mask
        mask = np.zeros((h, w), dtype=np.uint8)
        
        # Display image on canvas
        show_image_on_canvas(display_image, canvas)
        
        status_var.set(f"Image loaded: {os.path.basename(file_path)} ({w}x{h})")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")

def show_image_on_canvas(image, target_canvas):
    """Display image on specified canvas"""
    # Convert numpy array to PIL Image
    pil_image = Image.fromarray(image)
    
    # Convert to PhotoImage for tkinter
    photo = ImageTk.PhotoImage(pil_image)
    
    # Update canvas
    target_canvas.delete("all")
    target_canvas.config(width=pil_image.width, height=pil_image.height)
    target_canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    
    # Keep a reference to prevent garbage collection
    target_canvas.image = photo

def start_draw(event):
    """Start drawing mask when mouse is pressed"""
    global drawing, last_x, last_y
    if original_image is None:
        return
    drawing = True
    last_x = event.x
    last_y = event.y

def draw_mask(event):
    """Draw mask while mouse is dragged"""
    global drawing, last_x, last_y
    if not drawing or original_image is None:
        return
    
    # Draw on canvas (visual feedback)
    canvas.create_oval(
        event.x - brush_size//2, event.y - brush_size//2,
        event.x + brush_size//2, event.y + brush_size//2,
        fill="red", outline="red", stipple="gray50"
    )
    
    # Update mask (convert canvas coordinates to image coordinates)
    img_x = int(event.x / scale_factor)
    img_y = int(event.y / scale_factor)
    
    # Draw on actual mask
    cv2.circle(mask, (img_x, img_y), 
              max(1, int(brush_size / (2 * scale_factor))), 
              255, -1)
    
    last_x = event.x
    last_y = event.y

def stop_draw(event):
    """Stop drawing when mouse is released"""
    global drawing
    drawing = False

def clear_mask():
    """Clear the mask and redraw original image"""
    global mask
    if original_image is None:
        messagebox.showwarning("Warning", "Please load an image first!")
        return
    
    # Reset mask
    mask = np.zeros_like(mask)
    
    # Redraw original image on canvas
    show_image_on_canvas(display_image, canvas)
    
    status_var.set("Mask cleared")

def perform_inpainting():
    """Apply inpainting algorithm to remove objects"""
    global result_image
    if original_image is None:
        messagebox.showwarning("Warning", "Please load an image first!")
        return
    
    if np.sum(mask) == 0:
        messagebox.showwarning("Warning", "Please draw on the image to mark objects for removal!")
        return
    
    try:
        status_var.set("Processing... Please wait...")
        root.update()
        
        # Convert RGB back to BGR for OpenCV processing
        cv_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR)
        
        # Choose algorithm
        if algorithm_var.get() == "TELEA":
            algorithm = cv2.INPAINT_TELEA
            algo_name = "TELEA"
        else:
            algorithm = cv2.INPAINT_NS
            algo_name = "Navier-Stokes"
        
        # Perform inpainting
        result_bgr = cv2.inpaint(cv_image, mask, 3, algorithm)
        
        # Convert back to RGB
        result_image = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)
        
        # Resize for display
        h, w = result_image.shape[:2]
        display_w = int(w * scale_factor)
        display_h = int(h * scale_factor)
        result_display = cv2.resize(result_image, (display_w, display_h))
        
        # Show result
        show_image_on_canvas(result_display, result_canvas)
        
        status_var.set(f"Inpainting completed using {algo_name} algorithm!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Inpainting failed: {str(e)}")
        status_var.set("Inpainting failed")

def save_result():
    """Save the processed result image"""
    if result_image is None:
        messagebox.showwarning("Warning", "No result to save! Please perform inpainting first.")
        return
    
    file_path = filedialog.asksaveasfilename(
        title="Save Result",
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg"),
            ("All files", "*.*")
        ]
    )
    
    if not file_path:
        return
    
    try:
        # Convert RGB to BGR for saving
        result_bgr = cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(file_path, result_bgr)
        status_var.set(f"Result saved: {os.path.basename(file_path)}")
        messagebox.showinfo("Success", "Image saved successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {str(e)}")

def create_demo_image():
    """Create a demo image with simple shapes for testing"""
    demo_img = np.ones((300, 400, 3), dtype=np.uint8) * 255  # White background
    
    # Add some colored shapes to remove
    cv2.rectangle(demo_img, (50, 50), (150, 150), (255, 0, 0), -1)  # Red rectangle
    cv2.circle(demo_img, (300, 100), 50, (0, 255, 0), -1)  # Green circle
    cv2.ellipse(demo_img, (200, 200), (80, 40), 45, 0, 360, (0, 0, 255), -1)  # Blue ellipse
    
    # Add some texture
    noise = np.random.randint(0, 50, (300, 400, 3), dtype=np.uint8)
    demo_img = cv2.add(demo_img, noise)
    
    return demo_img

def load_demo_image():
    """Load a demo image for testing"""
    global original_image, display_image, mask, scale_factor
    
    try:
        # Create demo image
        original_image = create_demo_image()
        
        # Calculate scale factor for display
        canvas_width = 400
        canvas_height = 400
        
        h, w = original_image.shape[:2]
        scale_factor = min(canvas_width/w, canvas_height/h)
        
        # Resize for display
        display_w = int(w * scale_factor)
        display_h = int(h * scale_factor)
        display_image = cv2.resize(original_image, (display_w, display_h))
        
        # Initialize mask
        mask = np.zeros((h, w), dtype=np.uint8)
        
        # Display image on canvas
        show_image_on_canvas(display_image, canvas)
        
        status_var.set("Demo image loaded (400x300) - Draw over colored shapes to remove them!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create demo image: {str(e)}")

def setup_gui():
    """Create and setup the GUI"""
    global root, canvas, result_canvas, status_var, brush_scale, brush_label, algorithm_var
    
    # Create main window
    root = tk.Tk()
    root.title("Object Removal Tool - Inpainting (Functional Version)")
    root.geometry("1200x800")
    root.configure(bg='#f0f0f0')
    
    # Main frame
    main_frame = tk.Frame(root, bg='#f0f0f0')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Title
    title_label = tk.Label(main_frame, text="🎨 Object Removal with Inpainting", 
                          font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#333')
    title_label.pack(pady=10)
    
    # Control panel
    control_frame = tk.Frame(main_frame, bg='#e0e0e0', relief=tk.RAISED, bd=2)
    control_frame.pack(fill=tk.X, pady=10)
    
    # File operations
    file_frame = tk.Frame(control_frame, bg='#e0e0e0')
    file_frame.pack(side=tk.LEFT, padx=10, pady=10)
    
    tk.Button(file_frame, text="📁 Load Image", command=load_image,
             font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white',
             relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=5)
    
    tk.Button(file_frame, text="🎭 Demo Image", command=load_demo_image,
             font=('Arial', 12, 'bold'), bg='#FF9800', fg='white',
             relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=5)
    
    tk.Button(file_frame, text="💾 Save Result", command=save_result,
             font=('Arial', 12, 'bold'), bg='#2196F3', fg='white',
             relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=5)
    
    # Brush controls
    brush_frame = tk.Frame(control_frame, bg='#e0e0e0')
    brush_frame.pack(side=tk.LEFT, padx=20, pady=10)
    
    tk.Label(brush_frame, text="Brush Size:", font=('Arial', 10, 'bold'),
            bg='#e0e0e0').pack(side=tk.LEFT)
    
    brush_scale = tk.Scale(brush_frame, from_=5, to=50, orient=tk.HORIZONTAL,
                          command=update_brush_size, bg='#e0e0e0')
    brush_scale.set(20)
    brush_scale.pack(side=tk.LEFT, padx=5)
    
    brush_label = tk.Label(brush_frame, text="20px", font=('Arial', 10),
                          bg='#e0e0e0', width=5)
    brush_label.pack(side=tk.LEFT)
    
    # Algorithm selection
    algo_frame = tk.Frame(control_frame, bg='#e0e0e0')
    algo_frame.pack(side=tk.LEFT, padx=20, pady=10)
    
    tk.Label(algo_frame, text="Algorithm:", font=('Arial', 10, 'bold'),
            bg='#e0e0e0').pack(side=tk.LEFT)
    
    algorithm_var = tk.StringVar(value="TELEA")
    algo_combo = ttk.Combobox(algo_frame, textvariable=algorithm_var,
                             values=["TELEA", "NS"], state="readonly", width=8)
    algo_combo.pack(side=tk.LEFT, padx=5)
    
    # Action buttons
    action_frame = tk.Frame(control_frame, bg='#e0e0e0')
    action_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    
    tk.Button(action_frame, text="🧹 Clear Mask", command=clear_mask,
             font=('Arial', 12, 'bold'), bg='#FF5722', fg='white',
             relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=5)
    
    tk.Button(action_frame, text="✨ Remove Objects", command=perform_inpainting,
             font=('Arial', 12, 'bold'), bg='#9C27B0', fg='white',
             relief=tk.RAISED, bd=3).pack(side=tk.LEFT, padx=5)
    
    # Canvas frame
    canvas_frame = tk.Frame(main_frame, bg='#f0f0f0')
    canvas_frame.pack(fill=tk.BOTH, expand=True)
    
    # Original image canvas
    left_frame = tk.Frame(canvas_frame, bg='#f0f0f0')
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
    
    tk.Label(left_frame, text="Original + Mask (Draw to mark objects for removal)",
            font=('Arial', 12, 'bold'), bg='#f0f0f0').pack()
    
    canvas = tk.Canvas(left_frame, bg='white', relief=tk.SUNKEN, bd=2)
    canvas.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # Bind mouse events for drawing
    canvas.bind("<Button-1>", start_draw)
    canvas.bind("<B1-Motion>", draw_mask)
    canvas.bind("<ButtonRelease-1>", stop_draw)
    
    # Result canvas
    right_frame = tk.Frame(canvas_frame, bg='#f0f0f0')
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
    
    tk.Label(right_frame, text="Result (After object removal)",
            font=('Arial', 12, 'bold'), bg='#f0f0f0').pack()
    
    result_canvas = tk.Canvas(right_frame, bg='white', relief=tk.SUNKEN, bd=2)
    result_canvas.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # Status bar
    status_var = tk.StringVar()
    status_var.set("Load an image or try demo image to begin...")
    status_bar = tk.Label(main_frame, textvariable=status_var,
                         relief=tk.SUNKEN, anchor=tk.W, font=('Arial', 10),
                         bg='#d0d0d0')
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Instructions
    instructions = """
Instructions:
1. Click 'Load Image' to select your image or 'Demo Image' to try with sample shapes
2. Use mouse to draw/paint over objects you want to remove (red overlay shows your mask)
3. Adjust brush size as needed for precision
4. Choose inpainting algorithm: TELEA (faster) or NS/Navier-Stokes (better quality)
5. Click 'Remove Objects' to apply inpainting algorithm
6. Save the result when satisfied with the output

Tips: 
• TELEA works well for most cases and is faster
• Navier-Stokes (NS) may give better results for complex textures but takes longer
• Use smaller brush for detailed areas, larger brush for big objects
    """
    
    info_label = tk.Label(main_frame, text=instructions, font=('Arial', 9),
                         bg='#f0f0f0', fg='#666', justify=tk.LEFT)
    info_label.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

def main():
    """
    Object Removal Tool using OpenCV Inpainting Algorithms
    Functional Programming Version (No Classes/OOP)
    
    This tool provides an interactive GUI for removing unwanted objects from images
    using advanced computer vision inpainting techniques.
    
    Features:
    - Interactive drawing interface for marking objects to remove
    - Two inpainting algorithms: TELEA and Navier-Stokes
    - Adjustable brush size for precision marking
    - Side-by-side comparison of original and processed images
    - Demo image generator for testing
    - Support for common image formats (PNG, JPEG, BMP, TIFF)
    
    Requirements:
    pip install opencv-python numpy tkinter pillow
    
    How it works:
    1. Load an image or create a demo image
    2. Draw a mask over objects you want to remove (shows as red overlay)
    3. Choose inpainting algorithm:
       - TELEA: Fast Marching Method (faster, good for most cases)
       - NS: Navier-Stokes based (slower, better for complex textures)
    4. Apply inpainting to seamlessly remove marked objects
    5. Save the processed result
    
    The inpainting algorithms work by:
    - Analyzing the surrounding pixels around the masked area
    - Using mathematical models to predict what should be there
    - Filling in the masked regions with plausible pixel values
    - Creating seamless transitions that look natural
    """
    
    # Setup and run GUI
    setup_gui()
    
    print("Object Removal Tool Started!")
    print("Instructions:")
    print("1. Load an image or try the demo")
    print("2. Draw over objects to remove")
    print("3. Choose algorithm and click 'Remove Objects'")
    print("4. Save your result")
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()