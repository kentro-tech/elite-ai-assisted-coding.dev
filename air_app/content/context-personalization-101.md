# Optimize Your Dev Setup For Evals w/ Cursor Rules & MCP

In this guide, I'll show you how to optimize your development environment for AI-assisted coding using Cursor Rules and the Model Context Protocol (MCP).

## Why Context Matters

When working with AI coding assistants, the quality of the context you provide directly impacts the quality of the assistance you receive. By optimizing your context, you can:

1. Get more accurate code completions
2. Reduce hallucinations
3. Make the AI understand your codebase better
4. Speed up your development workflow

## Setting Up Cursor Rules

Cursor Rules allow you to define how your codebase should be interpreted by the AI. Here's how to set them up:

### Step 1: Create a .cursor.json file

In the root of your project, create a file named `.cursor.json` with the following structure:

```json
{
  "rules": [
    {
      "pattern": "**/*.py",
      "context": ["src/**/*.py", "tests/**/*.py"]
    },
    {
      "pattern": "**/*.js",
      "context": ["src/**/*.js", "src/**/*.jsx"]
    }
  ]
}
```

### Step 2: Define Patterns

The `pattern` field uses glob syntax to match files you're working on. When you open a file that matches this pattern, Cursor will include the files specified in the `context` array.

### Step 3: Customize for Your Project

Adjust the patterns based on your project structure. For example, for a Django project:

```json
{
  "rules": [
    {
      "pattern": "myapp/views/**/*.py",
      "context": [
        "myapp/models.py",
        "myapp/urls.py",
        "myapp/forms.py"
      ]
    }
  ]
}
```

## Using Model Context Protocol (MCP)

MCP is a standardized way to provide context to AI models. Here's how to use it effectively:

### Basic MCP Structure

```
<context>
This is information I want the model to know but not modify.
</context>

Now, here's my actual request...
```

### Example: Providing API Documentation

```
<context>
# API Documentation
GET /users - Returns a list of users
POST /users - Creates a new user
GET /users/{id} - Returns a specific user
</context>

Write a function that fetches a user by ID using the API.
```

## Combining Cursor Rules with MCP

For the ultimate setup, combine both approaches:

1. Use Cursor Rules for automatic file context
2. Use MCP for specific instructions or documentation

### Example Workflow

1. Set up your `.cursor.json` with appropriate rules
2. When asking for complex changes, use MCP to provide additional context:

```
<context>
Our project follows these conventions:
- Use camelCase for variables
- Use PascalCase for classes
- All functions must have docstrings
</context>

Refactor this user authentication function to follow our conventions.
```

## Conclusion

By properly setting up Cursor Rules and using MCP, you can significantly improve your AI-assisted coding experience. The AI will have better context about your codebase, leading to more accurate and helpful suggestions.

Remember that context is king when working with AI coding assistants. The more relevant context you provide, the better results you'll get.