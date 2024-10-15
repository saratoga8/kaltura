Feature: TODO tasks management

  Background:
    Given user is at the tasks page

  Scenario: Adding the first task
    When user adds a task
    Then there is a single task

  Scenario: Adding multiple tasks
    When user adds multiple tasks
    Then there is a list of tasks

  Scenario: Completing a task
    When user adds a task
    And user completes the task
    Then there the completed task

  Scenario: Deleting a task
    When user adds a task
    And user deletes the task
    Then there is no tasks

  Scenario Outline: Filtering <filter> tasks
    When user adds a task "Done"
    And user completes the task "Done"
    And user adds a task "Active"
    And user filters <filter> tasks
    Then there is the task "<filtered_task>"

    Examples:
       | filtered_task | filter    |
       | Done          | COMPLETED |
       | Active        | ACTIVE    |

  Scenario: Filtering all tasks
    When user adds a task "Done"
    And user completes the task "Done"
    And user adds a task "Active"
    And user filters ALL tasks
    Then there is the tasks: Done, Active

  Scenario: Edit task name
    When user adds a task "Old"
    And user renames the task to "New"
    Then there is the task "New"

  Scenario: Clear all completed tasks
    When user adds a task "Done"
    And user completes the task "Done"
    And user adds a task "Active"
    And user clears all completed tasks
    Then there is no completed tasks