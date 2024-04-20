# ***Project Name: Why So Cold?***
## ***Team members: Benjamin Zhang, Zhijie Kuang, Yzer De Gula***

---

### Sec 1. Introduction
Oftentimes when needing to take group photos, people usually ask strangers for help as you would need to be a good distance away from the photo to fit everyone into the picture. In our project, our goal is to use computer vision to solve this problem, with the activation being facial detection for smiling. It wouldn’t be a good group photo if someone is just angry in the corner right? This will solve the problem of being too out of reach to press the “take a picture” button on the camera app, and needing to run or wait awkwardly while using the “camera timer” feature. It will also provide a fun and interactive experience to incentivize people to take more and cheerier group photos, tackling 2 problems and solving them within the same app.

### Sec 2. Technical Approach
How we approach this is to first get video input so that we can detect and calculate the person’s smile in frame. To do this, we can utilize OpenCV’s eigenfaces algorithm, which utilizes PCA, to load and read the camera. We can also set the dimensions of the video of the webcam and wait for a user input to stop the feed. In order for us to implement the feature to take a picture when everyone in the designated scene is smiling, we'll first use facial recognition to get every face in the scene. Then, for every face, we detect the mouth within the face and if the mouth is above a certain angle value in the positive direction (positive being facing up rather than down, which will be frowning), the person is marked as smiling. If everyone in the scene has a “smiling” mark, then the picture will be taken.

### Sec 3. Milestones
- (4/11/2024): Set up github and project
- (4/19/2024): Make a rough sketch of facial recognition
- (4/26/2024): Implementation of the project
- (5/3/2024): Testing and debugging
- (5/10/2024): Finishing up the project and prepare for the demo
