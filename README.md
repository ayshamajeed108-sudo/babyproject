<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Baby Product Safety Analyzer 🎯

## Basic Details

### Team Name: Bitbybit

### Team Members
- Member 1: Biniya Rose - Vidya Academy of Science and Technology
- Member 2: Aysha Abdul Majeed - Vidya Academy of Science and Technology

### Hosted Project Link
https://babyproject-h3tm.onrender.com/

### Project Description
The Baby Product Safety Analyzer is an interactive data-driven dashboard that helps parents and caregivers verify the safety status of infant gear. It utilizes a synthetic dataset of 1,000+ records to simulate real-world safety certifications, recall alerts, and hazard identifications across categories like Sleep, Travel, and Toys.

### The Problem statement
With thousands of baby products on the market, parents often struggle to track active recalls or understand complex safety standards (like ASTM or CPSC). Fragmented information makes it difficult to quickly verify if a specific second-hand item or gift meets current safety regulations, leading to potential risks like suffocation or choking hazards.

### The Solution
This project provides a centralized, searchable interface built with Streamlit and Python. By clicking a single button, the system generates a comprehensive safety database. Users can then instantly query any product to receive a "Safety Analysis" report that includes certification details, age-appropriateness, and specific safety tips to mitigate common hazards.

---

## Technical Details

### Technologies/Components Used

**For Software:**
-Languages used: Python (3.9+)
-Frameworks used: Streamlit (for the Web UI)
-Libraries used: * pandas: For data manipulation and search filtering.
-json: For data structure handling.
-random: For synthetic data generation.
-Tools used: VS Code, Git/GitHub, Streamlit Cloud (for deployment).


---

## Features

List the key features of your project:

Instant Data Generation: A one-click mechanism to populate a mock database of 1,000 unique safety records using weighted probability (e.g., 5% recall rate).
Intelligent Search: A case-insensitive search engine that allows users to find products by brand name or item type (Crib, Stroller, etc.).
Visual Safety Status: A color-coded reporting system (Green for Verified Safe, Yellow for Alerts, Red for Active Recalls) for immediate risk assessment.
Hazard Awareness: Dynamically maps specific hazards (like "Positional Asphyxia" or "Choking Hazard") to products based on their safety status.
Safety Tip Integration: Provides actionable manufacturer-style advice for every product queried to ensure proper setup and usage.

---

## Implementation

### For Software:

#### Installation
First, ensure you have Python installed, then install the two necessary libraries:

Bash
pip install streamlit pandas

#### Run
Navigate to the folder containing your script (e.g., app.py) and launch the Streamlit server:

Bash
streamlit run app.py



---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Screenshot1]Dashboard Overview: This shows the landing page before data generation, prompting the user to initialize the safety database.

![Screenshot2]Product Safety Report: Displays the color-coded status (e.g., Green for "Verified Safe") and the detailed breakdown of certifications like ASTM and CPSC.

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
User Interface: Built with Streamlit, providing a reactive frontend for user inputs.

Application Logic: Python backend handles the weighted random generation of safety data.

Data Layer: Uses Pandas DataFrames stored in st.session_state for high-speed in-memory searching and filtering without needing an external database.

Output Engine: Transforms raw JSON-like data into visual alerts (Success/Warning/Error boxes) for the end-user.

**Application Workflow:**

![Workflow](docs/workflow.png)


#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

  
#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```


### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
