# Automated Newsletter Creation and Distribution System

## Overview
This system automates the process of creating and distributing newsletters. It utilizes GPT-4 for drafting newsletter content, DALL-E 3 for generating relevant images, and SMTP for sending the final newsletter via email. The process is streamlined through a series of tasks executed within a linear pipeline, making it efficient and scalable for various content creation and distribution needs.

## Dependencies
- Python 3.x
- OpenAI API key for GPT-4 and DALL-E 3
- SMTP server credentials (email and password)
- lyzr_automata library for task and pipeline management

## Flow of the code
- **Initialize Models:** Two OpenAI models are initialized; one for generating text (GPT-4) and another for creating images (DALL-E 3).
- **Create Newsletter Content:** A task is defined to draft newsletter content focused on a specific topic, utilizing the GPT-4 model.
- **Generate Image:** Another task uses DALL-E 3 to create an image relevant to the newsletter content.
- **Merge Content and Image:** A task is defined to merge the generated text and image into a single HTML email format.
- **Send Email:** The final task utilizes SMTP to send the merged newsletter to a list of email IDs.
- **Execute Pipeline:** A linear synchronization pipeline is set up to execute the tasks in sequence, from content creation to email distribution.

## How to Run
1. Ensure all dependencies are installed and you have an OpenAI API key along with SMTP server credentials.
2. Update the `config.py` file with your OpenAI API key, SMTP credentials (EMAIL, PASSWORD), and other necessary configurations.
3. Run the script by executing the `main_program()` function. This will sequentially execute the tasks for drafting content, generating an image, merging them, and sending the email.
4. Check the specified email addresses to confirm receipt of the newsletter.

This system streamlines the newsletter creation and distribution process, making it an efficient tool for marketers, content creators, and businesses looking to automate their email campaigns.