# AI-Singapore-Hackathon

Using PeekingDuck from AISingapore's Bricks.

Input: Webcam (if you are doing it on the computer); Model: "hr net" and "mtcnn"; Output: CLI or Terminal.

In this hackathon, I am a using a Windows computer and has created a file in the Windows C Drive, called "safebikeAI".
With the libraries, "gTTs" and "playsound" installed. The libraries are also cross-platform (available for both Windows and Macs).

At the start in the folder "safebikeAI", I have created another sub-folder "custom_node".
Inside the custom_node folder, there is one other sub-folder "src" and also, it contains the "run_config.yml" file.

In the "src" folder, there is a sub-folder "head_orientation", and it also contains two other sub-folders of "configs" and "output".
in the "configs" sub-folder, there will be another file called "output" that contains the "head_orientation.yml" file.
In the "output" sub-folder, it will contain the "head_orientation.py" file.

With all the files being in the right place, open the Command Line Interface (CLI) for Windows or Terminal for MacOs.

For Windows; In the CLI, use cd back to "C:\safebikeAI\custom_node" and then run the command "peekingduck run --config_path run_config.yml".
After the command has finished running, the application of the webcam of your computer will open and it will start to display a yellow box around your face, along with the red key points detections on your nose, left eye and right eye.

If there is a detection, you will hear the audio output of "Watch the road!", as well as with the display of the confidence level of the keypoints. If there isn't, the confidence level will show a low value.

This is useful, if you're a cyclist who has an addiction to their phone and needs facilities to help to focus on the road.
