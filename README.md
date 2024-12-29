# Magic Cloak
 <h1>Invisibility Cloak with OpenCV</h1>
    <p>This project implements a Harry Potter-style <strong>Invisibility Cloak</strong> using Python and OpenCV. It uses real-time video processing to detect a specific color (e.g., black) in a video feed and replaces it with a previously captured background, creating the illusion of invisibility.</p>

  <h2>Features</h2>
    <ul>
        <li>Real-time cloak detection using color segmentation.</li>
        <li>Supports user-defined cloak colors (e.g., black, red, blue).</li>
        <li>Works with any webcam or connected camera.</li>
        <li>Implements background subtraction and image masking.</li>
    </ul>

   <h2>How It Works</h2>
    <ol>
        <li>The program captures a static <strong>background image</strong> without the user in the frame.</li>
        <li>It detects the user’s cloak using the <strong>HSV color space</strong> and creates a mask for that specific color.</li>
        <li>The cloak area is replaced with the captured background using <strong>image masking techniques</strong>, making the cloak appear invisible.</li>
    </ol>

  <h2>Installation</h2>
    <h3>1. Prerequisites</h3>
    <p>Ensure you have the following installed:</p>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>pip (Python package manager)</li>
        <li>OpenCV library</li>
    </ul>

  <h3>2. Clone the Repository</h3>
    <pre><code>git clone https://github.com/hpishwe/magic-cloak.git
cd magic-cloak</code></pre>

   <h3>3. Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

   <h2>Usage</h2>
    <h3>Step 1: Capture the Background</h3>
    <pre><code>python cloak_detection.py</code></pre>
    <p>Follow the instructions:</p>
    <ol>
        <li>Stand <strong>out of the frame</strong> for a few seconds to let the program capture the background.</li>
        <li>Once the background is captured, step into the frame wearing your cloak (black color in this version).</li>
    </ol>

  <h3>Step 2: Make the Cloak Invisible</h3>
    <p>The script will detect the black cloak and replace it with the background, making it appear invisible in real-time.</p>

  
   

  <h2>Dependencies</h2>
    <p>The project uses the following Python libraries:</p>
    <ul>
        <li><strong>OpenCV</strong>: For image processing and video handling.</li>
        <li><strong>NumPy</strong>: For array operations and mask creation.</li>
    </ul>
    <p>These dependencies are included in the <code>requirements.txt</code> file.</p>

   
   <h2>Troubleshooting</h2>
    <ul>
        <li><strong>Edges of the cloak are visible</strong>: Adjust the HSV range to ensure complete color coverage.</li>
        <li><strong>Cloak detection is inconsistent</strong>: Improve lighting and avoid shadows or wrinkles on the cloth.</li>
        <li><strong>Script not working</strong>: Ensure you’ve installed all dependencies and your webcam is functional.</li>
    </ul>

   <h2>Future Improvements</h2>
    <ul>
        <li>Allow dynamic color selection for the cloak.</li>
        <li>Use deep learning models for more robust and precise segmentation.</li>
        <li>Add support for multiple cloaks in the same frame.</li>
    </ul>




    
</body>
</html>
