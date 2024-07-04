## Flask Application Design for Effective Time Management Tool

**HTML Files:**

- **index.html**: Landing page of the application, where users can provide input tasks and time slots.
- **schedule.html**: Displays the personalized schedule generated based on user input.
- **settings.html**: Allows users to adjust and customize their schedule as needed.

**Routes:**

- **/add_task**: Receives task inputs (name, description, start time, end time) from the user and adds them to the database.
- **/generate_schedule**: Generates the personalized schedule based on the tasks entered by the user and renders the schedule on the **schedule.html** page.
- **/edit_task**: Allows users to edit existing tasks, including name, description, and time slots.
- **/delete_task**: Facilitates users to remove tasks from their schedule.
- **/clear_schedule**: Clears all tasks from the schedule, resetting it to an empty state.
- **/settings**: Renders the **settings.html** page, where users can set preferences such as theme, font size, etc.