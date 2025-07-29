# Deployment Instructions for Railway

## Prerequisites
- A Railway account
- Your code pushed to a GitHub repository

## Deployment Steps

1. **Connect to Railway**
   - Log in to Railway.app
   - Create a new project
   - Choose "Deploy from GitHub repo"
   - Select your repository

2. **Set Environment Variables**
   - In Railway dashboard, go to your service settings
   - Add the following environment variable:
     ```
     BASE_URL=https://your-app-name.up.railway.app
     ```
   - Replace `your-app-name` with your actual Railway app subdomain

3. **Deploy**
   - Railway will automatically deploy when you push to your main branch
   - The app will be available at the URL shown in Railway dashboard

## Important Notes

- The `PORT` environment variable is set automatically by Railway
- Make sure to update `BASE_URL` with your actual domain for social cards to work
- The app uses Python 3.13 as specified in runtime.txt
- Static files are served from the `/static` directory

## Social Cards

Social card images must be accessible via absolute URLs. The app automatically converts relative image paths to absolute URLs using the `BASE_URL` environment variable.

## Health Check

The app includes a health check endpoint at `/health` for monitoring.