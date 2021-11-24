ol_openedx_canvas_integration
=============================

Overview
--------

A django app plugin for edx-platform to enable ``Rapid Response`` reports download functionality in ``Instructor`` tab.


**NOTE:**

Since the edx-platform’s ``Instructor Dashboard`` does not support the plugin based tab extensions so we had to make some changes in the edx-platform itself to add ``Rapid Responses`` tab through this plugin.
So, the ``edx-platform`` branch/tag you're using must include below commit for ``ol-openedx-rapid-response`` plugin to work properly:

- https://github.com/mitodl/edx-platform/commit/f6c7cc6ea528819e8779e3137c806911a81a3198

Installation
------------

You can install it into any Open edX instance by using any of the following methods:

- To get the latest stable release from PyPI


.. code-block::

    pip install ol-openedx-rapid-response


- To create a build locally and install it

.. code-block::

    # Open Terminal

    1. Navigate to "open-edx-plugins" directory
    2. Run ./pants build  # Do this if you haven’t run it already
    3. Run ./pants package ::  # This will create a "dist" directory inside "open-edx-plugins" directory with ".whl" & ".tar.gz" format packages for all the "ol_openedx_*" plugins in "open-edx-plugins/src")
    4. Install the "ol-openedx-rapid-response" using any of ".whl" or ".tar.gz" files generated in the above step

Dependencies
---------------

Since this plugin adds support for the `Rapid Response xBlock <https://github.com/mitodl/rapid-response-xblock>`_ report downloads so you need have that installed in order to use this plugin.

To install the Rapid Response xBlock you can simply use:

.. code-block::

    pip install rapid-response-xblock


How To Use
----------

1) Install ``rapid-response-xblock``

2) Install ``ol-openedx-rapid-response`` plugin

3) Follow the instructions on https://github.com/mitodl/rapid-response-xblock and create multiple choice problems and add some responses

4) Log into the LMS with an admin/staff, open a course having rapid response problems and click ``Instructor`` tab

5) You should now see ``Rapid Responses`` tab inside instructor tab

6) Click the ``Rapid Responses`` tab and you should see a list of ``Timestamped Links``, upon clicking any link a CSV report file should be downloaded

