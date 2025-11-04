# Car_Animation_Project
A stunning Tkinter-based animation showcasing different car rental scenarios for EuropCar. This project features smooth animations, transitions, and storytelling through visual elements.

Overview
This is an animated presentation built with Python's Tkinter library that showcases various car rental scenarios:

Airport arrivals
Land trips with bigger vehicles
Business car services
Mountain/adventure trips with 4x4s
Romantic occasions with convertibles

The animation runs through 11 slides with smooth transitions and culminates in a branded finale.
📦 Requirements
Software Requirements

Python 3.7 or higher
pip (Python package manager)

Python Libraries
tkinter (usually comes with Python)
pygame==2.6.1
PIL/Pillow==10.0.0
🚀 Installation
Step 1: Install Python
Download and install Python from python.org
Step 2: Install Required Libraries
Open Command Prompt/Terminal and run:
bashpip install pygame pillow
Step 3: Generate Images
Run the image generator script first to create all required images:
bashpython generate_images.py
This will create 15 PNG images in your current directory:

image1.PNG through image8e.PNG

Step 4: Organize Files
Make sure your project structure looks like this:
Desktop/Tkinter/
├── car1.py (main animation file)
├── generate_images.py
├── README.md
├── image1.PNG
├── image2.PNG
├── image3.PNG
├── image4.PNG
├── image5.PNG
├── image6.PNG
├── image6b.PNG
├── image6c.PNG
├── image6d.PNG
├── image6e.PNG
├── image7.PNG
├── image7b.PNG
├── image8.PNG
├── image8b.PNG
├── image8c.PNG
├── image8d.PNG
└── image8e.PNG
🎮 Usage
Running the Animation
Method 1: Command Line
bashcd C:\Users\praty\OneDrive\Desktop\Tkinter
python car1.py
Method 2: Python IDLE

Open car1.py in IDLE
Press F5 or Run → Run Module

Method 3: Double Click

Simply double-click car1.py (if .py files are associated with Python)

Adding Sound (Optional)

Download a car engine sound as carsound.mp3
Place it in the same folder as car1.py
Uncomment these lines in the code:

pythonpygame.mixer.music.load("carsound.mp3")
pygame.mixer.music.play()
📁 Project Structure
Main Files
car1.py - Main animation script containing:

firstslide() - Opening "sometimes" text
secondslide() - Airport scene introduction
thirdslide() - Small car presentation
fourthslide() - Green car view
fifthslide() - Bigger car for land trips
sixthslide() - Van presentation
seventhslide() - Business car with meeting scene
eighthslide() - 4x4 truck introduction
ninethslide() - Mountain scene
tenthslide() - Romantic convertible scene
eleventhslide() - Final branding and contact info

generate_images.py - Image generation script that creates all 15 required PNG files
Image Files

🎨 Customization
Changing Colors
The background color is set to sky blue (#33BEFF). To change it:
pythonw=Canvas(master, width=1000, height=1000, bg="#YOUR_COLOR")
Adjusting Animation Speed
Modify these values in each function:
pythontime.sleep(0.02)  # Lower = faster, Higher = slower
xspeed1=5         # Movement speed
Updating Contact Information
Edit the eleventhslide() function:
pythonline=w.create_text(480,330,text="Car Rental in YOUR_COUNTRY",...)
line=w.create_text(480,400,text="www.yourwebsite.com",...)
line=w.create_text(480,460,text="Mob: YOUR_NUMBER",...)
Creating Custom Images
Replace any image by editing generate_images.py and regenerating, or create your own PNG files with the same names.
🔧 Troubleshooting
Common Issues
Problem: "ModuleNotFoundError: No module named 'pygame'"
bashSolution: pip install pygame
Problem: "No file 'carsound.mp3' found"
pythonSolution: Comment out these lines:
# pygame.mixer.music.load("carsound.mp3")
# pygame.mixer.music.play()
Problem: "couldn't open image file"
Solution: 
1. Check that all PNG files are in the correct folder
2. Verify file paths in the code match your directory structure
3. Re-run generate_images.py to recreate missing images
Problem: Animation runs too fast/slow
pythonSolution: Adjust time.sleep() values in each function
# Slower animation
time.sleep(0.1)  # Instead of 0.05

# Faster animation  
time.sleep(0.01)  # Instead of 0.05
Problem: Window is too large/small
pythonSolution: Change canvas dimensions in the code
w=Canvas(master, width=800, height=800, bg="#33BEFF")
Getting Help
If you encounter issues:

Check that all image files exist in the correct location
Verify Python version is 3.7+
Ensure all required libraries are installed
Check file paths match your directory structure

🎓 Learning Points
This project demonstrates:

Tkinter Canvas: Creating and animating shapes and images
Animation Loops: Using while loops with timing controls
Image Handling: Loading and positioning images with PhotoImage
Coordinate Systems: Managing object positions and movements
Event Timing: Controlling animation flow with time.sleep()
PIL/Pillow: Generating graphics programmatically

📝 Notes

The animation automatically starts from slide 10. To start from the beginning, change the last line from tenthslide() to firstslide()
Each slide has its own timing and speed settings for unique visual effects
The final slide displays company branding and contact information
Images are stored as PNG files for transparency support
