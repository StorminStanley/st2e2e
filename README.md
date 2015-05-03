# StackStorm End-to-End Tests

## Pre-Requisites

1. Install firefox and Xvfb

On Ubuntu / Debian:

    ```
    sudo apt-get install firefox xvfb
    ```
    
On RedHat / Fedora:

    ```
    sudo yum -y install firefox Xvfb
    ```

2. Download tests

    ```
    git clone https://github.com/StackStorm/st2e2e
    cd st2e2e
    ```

## Running Tests

1. Run X Virtual FrameBuffer then export DISPLAY

    ```
    sudo Xvfb :10 -ac &
    export DISPLAY=:10
    ```

2. Run `make`.

  This will create virtualenv, install selenium and run the tests. If you need to run tests second time with requirements already installed, you can either run `make .tests` or

    ```
    . virtualenv/bin/activate
    python webui/test_st2web.py [host port]
    ```

By default, the tests will try to run on _localhost:8080_. To run tests on a different environment, specify host and port as arguments for the test.

## Tests

Tests use ``unittest`` framework. Currently 2 tests are available in the package:

### Test setup and teardown

Each test starts the browser, navigates to WebUI and logs in before running the test.
At the end of each test the browser is closed.

### test_run_action

1. Navigates to Actions tab
2. Starts ``core.local`` action, which executes ``uname`` command.
3. Waits for the Executions list to change to Status ``Succeeded``.
4. Switches to History and verifies the Status and Output of the command (expecting ``Succeeded`` and ``Linux``)

### test_web_trigger

1. Navigates to Rules tab
2. Removes all existing rules (this is required to achieve non-ambiguous results)
3. Creates the new rule with trigger ``core.st2.webhook`` and action ``core.local``
2. Checks that new rule is ``Enabled``
3. Issues an HTTP request, similar to one shown on Quick Start guide to activate the webhook. The request carries a unique ID, which makes sure the right request is checked in the history.
4. Switches to History and verifies that the Status is ``Succeeded`` and Trigger Payload contains a unique ID, issued in previous step. Also checks that the action, started  by a trigger returns expected output.

## Concepts

### Tests

The main objectives while writing the tests, are:

* **Readability**: anyone looking at the test should have a gist of what is tested and what is verified
* **Configurability**: unlike unit tests, the end-to-end tests must support running on different environments, including developer's machines.
* **Maintainability**: ensure that tests can be kept up-to-date with relative easiness. Important parts of this goal are: reusing the repetitive routines, specific to the application; having an abstraction (logical) level between application and underlying browser interaction, and isolating the most breakable code (related to the UI).

### Logging

The logs contain information useful for the following activities:

* Debugging the tests. This log is reported with
* Checking what test is doing in order to repeat operations manually
* Overall test status

Example of the log:

    >>> Start st2web on Firefox at http://localhost:9101/webui
          browser: Running on Firefox
          browser: Navigating to http://localhost:9101/webui
          web page: Wait for //div[contains(@class,"login")] to be present
    >>> Login
          browser: Navigating to http://localhost:9101/webui
          web page: Wait for //div[contains(@class,"login")] to be present
          web page: Wait for //input[contains(@class,"login__button")] to be clickable
          web element: Click
        Wait for History to load
          web page: Wait for //div[contains(@class,"panel__toolbar-title") and contains(text(), "History")] to be present
    <<< Logged-in successfully
        Switch to Actions
          web page: Wait for //a[contains(@href, "actions")] to be present
          web page: Wait for //a[contains(@href, "actions")] to be clickable
          web element: Click
    <...>
    ----------------------------------------------------------------------
    Ran 2 tests in 36.188s

    OK

The ``>>>`` sign marks repeatable steps someone can perform manually; ``<<<`` display the outcome of those steps, while test was running
The log lines with more indentation are for debugging
In the end the summary of the number of tests and overall status are provided by ``unittest`` framework

### Library Structure

The reusable code that can be shared by all tests is stored in the ``lib`` folder and has the following structure:

    /lib
     |--/web
           |--abstract*.py
           |--selenium*.py
           |--implementation_factory.py
     |--st2web*.py

* **/web** - general browser library
* **abstract*.py** - abstract definition of the browser, webpage, web element, and web page synchronization objects. Any implementation, that uses some library and extends those objects will be acceptable for the tests.
* **selenium*.py** - the selenium-specific implementation of the browser, webpage, web element, and web page synchronization objects.
* **implementation_factory.py** - allows to control a specific implementation of the library, without directly referring to it from the tests. For example, if test or application library needs to open Firefox, it would call:
    ``self.browser = ImplementationFactory().get_firefox()``
* **st2web*.py** - webui application library. The library contains of common functions and locators, the class that represents the application and representation of each page.

The tests will always use the application library only, thus changes in the UI can be fixed once per library, and the tests do not need to be changed. For example:

* If some xpath was changed, only ``st2web_locators`` file needs to be changed
* If pages change structure (e.g. navigation between tabs completely changes), ``st2web_locators`` and ``st2web_common`` may need to change
* If additional methods are required for Actions, only ``st2web_locators`` and ``st2web_actions_page`` will need to change
And so on

## Bugs and Limitations

Submitted as Issues in this repository, with _webui tests:_ prefix

## Copyright, License, and Contributors Agreement

Copyright 2015 StackStorm, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the [LICENSE](LICENSE) file, or at:

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

By contributing you agree that these contributions are your own (or approved by your employer) and you grant a full, complete, irrevocable copyright license to all users and developers of the project, present and future, pursuant to the license of the project.
