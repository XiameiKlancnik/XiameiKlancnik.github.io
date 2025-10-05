# Xiamei Klancnik - Portfolio Website

A modern, dark-themed portfolio website showcasing data science and ML engineering projects.

## 🌟 Features

- **Dark Theme Design**: Professional dark mode interface
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile
- **Project Demos**: Dedicated pages for Ingestigate and WorldVue AI projects
- **Smooth Animations**: Engaging scroll animations and transitions
- **SEO Optimized**: Clean HTML structure with semantic elements

## 📁 File Structure

```
├── index.html              # Main portfolio page
├── ingestigate-demo.html   # Ingestigate app demo page
├── worldvue-demo.html      # WorldVue AI demo page
├── styles.css              # All styling and dark theme
├── script.js               # Interactive features and animations
└── README.md              # This file
```

## 🚀 Hosting on GitHub Pages (FREE!)

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in (or create an account)
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name it: `your-username.github.io` (replace `your-username` with your actual GitHub username)
   - Example: If your username is "xklancnik", name it `xklancnik.github.io`
5. Make sure it's set to "Public"
6. Click "Create repository"

### Step 2: Upload Your Files

**Option A: Upload via GitHub Website**
1. In your new repository, click "uploading an existing file"
2. Drag and drop all 5 files:
   - `index.html`
   - `ingestigate-demo.html`
   - `worldvue-demo.html`
   - `styles.css`
   - `script.js`
3. Click "Commit changes"

**Option B: Upload via Command Line (if you have Git installed)**
```bash
# Navigate to the folder with your website files
cd /path/to/your/website/files

# Initialize Git
git init

# Add all files
git add .

# Commit the files
git commit -m "Initial portfolio website"

# Add your GitHub repository as remote
git remote add origin https://github.com/your-username/your-username.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" (top menu)
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select "main" branch
5. Click "Save"

### Step 4: Access Your Website

Your website will be live at: `https://your-username.github.io`

⏱️ **Note**: It may take 5-10 minutes for your site to go live the first time.

## 🎨 Customization

### Update Your Information

Edit `index.html` to change:
- Contact information (email, phone, location)
- Project descriptions
- Work experience dates
- Education details

### Change Colors

Edit `styles.css` and modify the CSS variables at the top:

```css
:root {
    --accent-primary: #10b981;     /* Main accent color */
    --accent-secondary: #06d6a0;   /* Secondary accent */
    /* ... other colors ... */
}
```

### Add More Projects

In `index.html`, find the projects section and add new project cards following the existing structure.

## 📱 Testing Locally

To test your website before uploading:

1. Simply open `index.html` in your web browser
2. Or use a local server:
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Then visit: http://localhost:8000
   ```

## 🔧 Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

## 📄 License

Feel free to use this template for your own portfolio!

## 🆘 Need Help?

If you encounter any issues:
1. Check that all file names match exactly (case-sensitive)
2. Ensure all files are in the same directory
3. Clear your browser cache
4. Wait 10-15 minutes after first deploying to GitHub Pages

## 🎯 Next Steps

1. Add actual screenshots of your apps to the demo pages
2. Consider adding a blog section
3. Include links to GitHub repositories
4. Add a downloadable CV/resume
5. Connect Google Analytics to track visitors

---

**Your website will be live at:** `https://your-username.github.io`

Replace `your-username` with your actual GitHub username!
