# 🖱️ Virtual Mouse - Hand Gesture Control System

A computer vision-powered application that lets you control your mouse cursor and perform clicks using hand gestures captured through your webcam.

## 🌟 Features

- **Mouse Control**: Move your cursor by pointing with your index finger
- **Left Click**: Bring your index and middle fingers close together
- **Right Click**: Touch your thumb and index finger together
- **Screenshot**: Open your palm (all fingers extended) to capture a screenshot
- **Real-time Hand Tracking**: Uses advanced computer vision to track hand movements
- **Safety Features**: Built-in fail-safes to prevent accidental actions

## 🛠️ Tech Stack

- **Python 3.9** - Core programming language
- **OpenCV** - Computer vision and camera handling
- **MediaPipe** - Google's hand landmark detection
- **PyAutoGUI** - Mouse control and automation
- **NumPy** - Mathematical operations and coordinate mapping
- **PyCaw** - Windows volume control (optional)

## 📋 Requirements

- Python 3.9 or higher
- Webcam
- Windows OS (for volume control features)
- Good lighting for optimal hand detection

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd VirtualMouse
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install opencv-python mediapipe pyautogui numpy pycaw comtypes
   ```

## 🎮 How to Use

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Position yourself**
   - Sit in front of your webcam
   - Ensure good lighting
   - Keep your hand visible in the camera frame

3. **Control your mouse**
   - **Move cursor**: Point with your index finger
   - **Left click**: Pinch index and middle fingers together
   - **Right click**: Touch thumb and index finger
   - **Screenshot**: Open your palm completely

4. **Exit the program**
   - Press `ESC` key to quit safely

## 🎯 Gesture Guide

| Gesture | Action | Description |
|---------|--------|-------------|
| 👆 Index pointing | Mouse movement | Move your index finger to control cursor |
| 🤏 Index + Middle pinch | Left click | Bring index and middle fingertips close |
| 👌 Thumb + Index touch | Right click | Touch thumb and index fingertips |
| ✋ Open palm | Screenshot | Extend all fingers to capture screen |

## ⚙️ Configuration

### Safety Settings
- **Fail-safe**: Move mouse to top-left corner to emergency stop
- **Pause**: 0.1-second delay between actions to prevent spam
- **Cooldowns**: Built-in delays for clicks and screenshots

### Camera Settings
- Default camera: Index 0 (primary webcam)
- Hand detection confidence: 70%
- Tracking confidence: 50%

## 🔧 Troubleshooting

### Common Issues

**Camera not working**
- Ensure no other applications are using the webcam
- Check camera permissions
- Try changing camera index in code if multiple cameras

**Poor hand detection**
- Improve lighting conditions
- Keep hand within camera frame
- Avoid background clutter
- Maintain steady hand movements

**Gestures not responding**
- Adjust detection confidence values
- Ensure clear finger positioning
- Check for proper finger spacing in gestures

### Performance Tips
- Close unnecessary applications for better performance
- Use good lighting for accurate detection
- Keep background simple and uncluttered
- Maintain steady hand movements

## 📁 Project Structure

```
VirtualMouse/
├── app.py              # Main application file
├── README.md          # This documentation
├── screenshot.png     # Sample screenshot output
├── venv/             # Virtual environment
└── .git/             # Git repository
```

## 🔒 Safety Features

- **Emergency stop**: Move cursor to screen corner
- **Click cooldowns**: Prevents accidental rapid clicking
- **Gesture validation**: Ensures proper hand positioning
- **Error handling**: Graceful handling of camera/system errors

## 🚨 Important Notes

- Keep your hand steady for better accuracy
- Ensure good lighting for optimal detection
- The system works best with a plain background
- Some features may require additional permissions
- Volume control requires PyCaw library (Windows only)

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving gesture recognition
- Adding cross-platform support

## 📄 License

This project is open source. Please ensure proper attribution when using or modifying the code.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section
2. Ensure all dependencies are installed
3. Verify camera functionality
4. Check lighting conditions

---

**Note**: This is an experimental project. Use responsibly and ensure proper lighting and positioning for best results.