# Cursor Tool Review

> A technical reference for Cursor's AI-assisted development features

## Overview

Cursor is a fork of VS Code that integrates AI assistance throughout the development workflow. It is worth trying because it is a full IDE that gives a great diff experience on AI changes, and is very aggressive with the AI assistance. Cursor is one of the tools I use day-to-day for coding and it's a great tool.

[![Course Card](/static/CourseCard.jpg)](https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC)

[**Enroll Now on Maven →**](https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC)

## Top IDE Features

### Tab Completion

Cursor's completions use project-wide context rather than just the current file and are very aggressive, which is good in some situations and annoying in others.

> **Helpful Use Case**
> I was doing an [OSS PR to add type hints](https://github.com/feldroy/air/pull/143/files#diff-e14fd0d1e563b32e21626eaeba650c79ce24651dfe03c83a5d977372384ff8ec) to a new web development framework called `air` (very repetitive task). These needed to be matched up to a HTML reference documentation, and agents kept leaving off or added tags. Cursor's tab completion let me copy/paste from reference docs then hit tab for it to tab complete and modify to python syntax very quickly. It got the pattern after the first couple and let me get through it all in very little time.

> **Unhelpful Use Case**
> I was working on creating examples for a workshop I was teaching on [FastHTML Syntax and Project Organization](https://github.com/kentro-tech/fasthtml-routes-and-syntax-ws/tree/main). The tab completion was extremely annoying, because it was project wide it kept trying to autocomplete and change my code to what I did somewhere else. I felt like I was fighting the tab completion constantly and having to keep telling it to go away A LOT because I had a very specific thing in mind I wanted to do.

### Chat/Agent Interface (`Cmd+L` `Cmd+I`)

Context-aware chat that understands project structure. This is pretty helpful with being able to easily reference lots of things with the `@` syntax for files. If you have code highlighted when you engage it that will be included in context specifically, and open files will also be in context for you.

> **Usage Tip**
> I find it really helpful to dump lots of things in a `ref` folder then `@` like everything useful as I go. This can be tutorials I found online, docs, etc. I can `@` the URL directly, but the `ref` folder serves as an aggregator for me that's a bit easier to keep top of mind and curate as needed than the cursor docs feature IMO.

The Agent gives many options and you get really nice diffs that you can individually review, or accept all, and you can restore back to checkpoints if you accepted changes that you find don't work well after testing.

### Inline Editor (`Cmd+K`)

Edit code in place with AI assistance `Cmd+K`. This lets you target specific pieces of code to edit. This is extremely helpful for limiting the scope of AI, especially when it's trying to do too much or you know exactly where the change should happen.

I often use this to quickly ask it to write a doc string for documentation, or to do things like refactor a hairy logic stuck inside loops or conditionals into functions.

### Terminal helped (also `Cmd+K`)

In your terminal you can select `Cmd+K` to have an AI assist that sees that terminals history. This is super helpful for lots of things, like telling you how to run things, git commands you've forgotten, telling it to do some curl command you don't remember all the flags you need, etc.

The **really** nice thing about `Cmd+K` is it's very controlled, so it puts the command in your terminal but YOU must run it. This makes it nice because I can ask it to help with even fairly risk things because it won't be running anything on it's own.

### Cursor Rules

Cursor Rules are extremely helpful and there's 4 modes:

![Cursor Rules Options](/static/CursorRulesOptions.png)

- **Always Apply** - Core rules that should never be violated
- **Apply Manually** - Rules you trigger when needed. If you're really bad at thinking about context, and you're not going to put a lot of effort in then don't use this.
- **Apply Intelligently** - This is a great thing to use and provide a good description for the agent to know when to use it.
- **Apply to Specific Files** - File-type or path-specific rules. This can be nice, but you're liable to set it to a path, restructure something, then forget and this rule will be accidentally deprecated. This is useful in a decently mature code base, or with very general paths like `src` or `docs` directory that are not likely to change.

## Additional Features

- Background Agents: These are great to bring some of what you do in cursor for easier tasks to run in parallel
- Slack/Github Integration: A nice features to do additional tasks and ask cursor to work on things from Slack or from a github repo. I didn't find it as useful for actual coding things, as I found going to the IDE, adding additional context and thinking about the task instructions for formulate payed dividends. But for writing tasks it was a great easy starting point!