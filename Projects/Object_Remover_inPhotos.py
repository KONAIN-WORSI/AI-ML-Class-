import cv2 as cv
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
scale_factor = 1.1
last_x, last_y = 0, 0

# Gui components
root = None
canvas = None
result_canvas = None
brush_scale = None
status_var = None
algorithm_var = None
brush_label = None

def update_brush_size(value):
    # update the brush size basde on the slider value
    global brush_size
    brush_size = int(value)
    brush_label.config(text = f'Brush Size: {brush_size}')


def load_image():
    # Load an image from files
    global original_image, display_image, mask, scale_factor

    file_path = filedialog.askopenfilename(title = 'Select an Image', 
                                           filetypes = [('Image Files', '*.jpg;*.jpeg;*.png;*.bmp*;*.tiff'),
                                                        ('All Files', '*.*')])
    
    if not file_path:
        raise ValueError('No file selscted.')
    
    original_image = cv.imread(file_path)

    if original_image is None:
        raise ValueError('Could not read the image file.')
    
    try:
        original_image = cv.cvtColor(original_image, cv.COLOR_BGR2RGB)
        
        # Creating canvas height and width
        canvas_height = 400
        canvas_width = 400 

        h, w = original_image.shape[:2]
        scale_factor = min(canvas_height/ h, canvas_width/ w)

        display_h = int(h * scale_factor)
        display_w = int(w * scale_factor)
        display_image = cv.resize(original_image, (display_w, display_h))

        # creating mask
        mask = np.zeros((h, w), dtype = np.uint8)

        # Display the image on the canvas
        show_image_on_canvas(display_image, canvas)

        status_var.set(f'Image Loaded: {os.path.basename(file_path)} {h}X{w}')
    except Exception as e:
        messagebox.showerror('Eror Loading Image', str(e))


def show_image_on_canvas(image, canvas):
    # convert the image to Photo Image format and display it on the canvas
    pil_image = Image.fromarray(image)

    photo = ImageTk.PhotoImage(pil_image)

    # display the image on the canvas
    canvas.delete('all')
    canvas.config(width = photo.width(), height = photo.height())
    canvas.create_image(0, 0, anchor = tk.NW, image = photo)

    canvas.image = photo # keep a reference to avoid garbage collection

def start_draw(event):
    # start drawing when mouse is pressd
    global drawing, last_x, last_y
    drawing = True
    last_x, last_y = event.x, event.y

def draw_mask(event):
    """Draw mask while mouse is dragged"""
    global drawing, last_x, last_y
    if not drawing or original_image is None:
        return
    
    # Draw on canvas (visual feedback)
    canvas.create_oval(
        event.x - brush_size//2, event.y - brush_size//2,
        event.x + brush_size//2, event.y + brush_size//2,
        fill="red", outline="red"
    )
    
    # Update mask (convert canvas coordinates to image coordinates)
    img_x = int(event.x / scale_factor)
    img_y = int(event.y / scale_factor)
    
    # Draw on actual mask
    cv.circle(mask, (img_x, img_y), 
              max(1, int(brush_size / (2 * scale_factor))), 
              255, -1)
    
    last_x = event.x
    last_y = event.y

def stop_draw(event):
    # stop drawing when mouse is released
    global drawing
    drawing = False

def clear_mask():
    # clear the mask 
    global mask, display_image

    if original_image is None:
        messagebox.showwarning('Warning', 'No image loaded to clear mask.')
    else:
        mask = np.zeros_like(mask)

        show_image_on_canvas(display_image, canvas)
        status_var.set('Mask Claered')

def perform_inpainting():
    # perform inpainting based on the selected algortihm
    global original_image, mask, result_image

    if original_image is None:
        messagebox.showwarning('Warning', 'No Image loaded for inpainting.')

    if np.sum(mask) == 0:
        messagebox.showwarning('Warning', 'Mask is empty. please draw on the image first to remove objects.')

    try:
        root.update()

        if algorithm_var.get() == 'TELEA':
            algorithm = cv.INPAINT_TELEA
            algo_name = 'TELEA'
        else:
            algorithm = cv.INPAINT_NS
            algo_name = 'NS'

        result_bgr = cv.inpaint(original_image, mask, 3, algorithm)

        result_image = cv.cvtColor(result_bgr, cv.COLOR_BGR2RGB)

         # resize the result image for display
        h = result_image.shape[0]
        w = result_image.shape[1]
        result_display = cv.resize(result_image, (int(w * scale_factor), int(h * scale_factor)))


        show_image_on_canvas(result_display, result_canvas)
        status_var.set(f'Inpainting completed using {algo_name} alogrithm.')
    except Exception as e:
        messagebox.showerror('Error', f'Inapainting failed: {str(e)}')


def save_result():
    # save the result image to a file
    global result_image

    if result_image is None:
        messagebox.showwarning('Warning', 'No result image to save.')

    file_path = filedialog.asksaveasfilename(
        title = 'Save Result Image',
        defaultextension = '.png',
        filetypes = [('PNG Files', '*.png'), ('JPEG Files', '*.jpg;*.jpeg'), ('All Files', '*.*')]
    )

    if not file_path:
        messagebox.showwarning('Warning', 'No file selected to save the resuult image')
        return
    
    try:
        result_bgr = cv.cvtColor(result_image, cv.COLOR_RGB2BGR)
        cv.imwrite(file_path, result_bgr)
        status_var.set(f'Result image saved as {os.path.basename(file_path)}')
        messagebox.showinfo('Success', 'Image saved successfully.')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to save the result image: {str(e)}')

def create_gui():
    global root, canvas, result_canvas, brush_scale, status_var, algorithm_var, brush_label

    # create the main window
    root = tk.Tk()
    root.title('Object Remover (using OpenCV Inpainting) Tool')
    root.geometry('1200x800')
    root.configure(bg = '#113537')

    # Main frame
    main_frame = tk.Frame(root, bg = '#FFEAD0')
    main_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)

    # title
    title_label = tk.Label(main_frame, text = 'Object Remover Tool', font = ('Arial', 24, 'bold'), bg = '#FFEAD0')
    title_label.pack(pady = 10)

    # control panel
    control_frame = tk.Frame(main_frame, bg = '#FFEAD0', relief = tk.RAISED, bd = 2)
    control_frame.pack(fill = tk.X, padx = 10, pady = 10)

    # file operations
    file_frame = tk.Frame(control_frame, bg = '#FFEAD0')
    file_frame.pack(side = tk.LEFT, padx = 10, pady = 10)

    # load buttons
    tk.Button(file_frame, text = '📁 Load Image', command = load_image,
               font = ('Arial', 12, 'bold'), bg = '#4CAF50', fg = 'White',
                relief = tk.RAISED).pack(side = tk.LEFT, fill = tk.X, padx = 10, pady = 10)
    
    
    tk.Button(file_frame, text = '💾 Save Result', command = save_result, 
              font = ('Arial', 12, 'bold'), bg = '#2196F3', fg = 'white',
              relief = tk.RAISED).pack(side = tk.RIGHT , fill = tk.X, padx = 10, pady = 10)
    

    # brush frame
    brush_frame = tk.Frame(control_frame, bg = '#FFEAD0')
    brush_frame.pack(side = tk.LEFT, padx = 10, pady = 10)

    tk.Label(brush_frame,font = ('Arial', 10, 'bold'), bg = '#FFEAD0').pack(side = tk.TOP, pady = 5)

    brush_scale = tk.Scale(brush_frame, from_ = 1, to = 50, orient = tk.HORIZONTAL, 
                           command = update_brush_size, bg = '#FFEAD0', fg = 'black',
                           font = ('Arial', 10, 'bold'))
    brush_scale.set(20) # default brush size

    brush_scale.pack(side = tk.RIGHT, fill = tk.X, padx = 10, pady = 10)
    brush_label = tk.Label(brush_frame, text = '20 px', 
                           font = ('Arial', 10, 'bold'), bg = '#FFEAD0')
    brush_label.pack(side = tk.RIGHT)

    # algorithm selection
    algo_frame = tk.Frame(control_frame, bg = '#FFEAD0')
    algo_frame.pack(side = tk.LEFT, padx = 10, pady = 10)

    tk.Label(algo_frame, text = 'Inpainting Algorithm: ', 
             font = ('Arial', 10, 'bold'), bg = '#FFEAD0').pack(side = tk.TOP, pady = 5)
    algorithm_var = tk.StringVar(value = 'TELEA') # default algorithm
    algo_combo = ttk.Combobox(algo_frame, textvariable = algorithm_var,
                              values = ['TELEA', 'NS'], state = 'readonly',
                              font = ('Arial', 10, 'bold'), width = 10)
    algo_combo.pack(side = tk.TOP, fill = tk.X, padx = 15, pady = 15) 
    
    # action frame
    action_frame = tk.Frame(control_frame, bg = '#ffead0')
    action_frame.pack(side = tk.LEFT, padx = 10, pady = 10)

    tk.Button(action_frame, text = '🧹 Clear Mask', command = clear_mask, 
              font = ('Arial', 12, 'bold'), bg = '#FF9800', fg = 'white',
              relief = tk.RAISED).pack(side = tk.LEFT, fill = tk.X, padx = 5, pady = 10)
    
    tk.Button(action_frame, text = '✨ Remove Objects', command = perform_inpainting,
              font = ('Arial', 12, ' bold'), bg = '#F44336', fg = 'white',
              relief = tk.RAISED).pack(side = tk.RIGHT, fill = tk.X, padx = 10, pady = 10)
    
    # canvas frame 
    canvas_frame = tk.Frame(main_frame, bg = '#f0f0f0')
    canvas_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)

    # canvas for original image
    left_canvas = tk.Frame(canvas_frame, bg = '#f0f0f0')
    left_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

    tk.Label(left_canvas, text = 'Original Image + Mask Interaction',
              font = ('Arial', 14, 'bold'), bg = '#f0f0f0').pack()
    
    canvas = tk.Canvas(left_canvas, bg = '#f0f0f0', relief = tk.RAISED, bd  = 2)
    canvas.pack(fill = tk.BOTH, expand = True, pady = 5)

    # bind mouse events for drawing
    canvas.bind('<Button-1>', start_draw)
    canvas.bind('<B1-Motion>', draw_mask)
    canvas.bind('<ButtonRelease-1>', stop_draw)

    # canvas for result image
    right_canvas = tk.Frame(canvas_frame, bg = '#f0f0f0')
    right_canvas.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

    tk.Label(right_canvas, text = 'Result Image (after Inpainting)', 
             font = ('Arial', 14, 'bold'), bg = '#f0f0f0').pack()
    
    result_canvas = tk.Canvas(right_canvas, bg = '#f0f0f0', relief = tk.RAISED, bd = 2)
    result_canvas.pack(fill = tk.BOTH, expand = True, pady = 5)

    # status bar
    status_var = tk.StringVar()
    status_var.set('Welcome to object remover tool. Load an image to start.')
    status_bar = tk.Label(root, textvariable = status_var, 
                          font = ('Arial', 10), bg = '#113537', fg = 'white')
    status_bar.pack(side = tk.BOTTOM, fill = tk.X)

     
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
    create_gui()


    root.mainloop()


if __name__ == '__main__':
    main()


    

    




    

  












