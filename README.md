# Printhat Queue
A simple CLI tool for managing a queue of gcode to be sent to one or more 3d printers,
making it easier to perform slicing in batches as time allows - and printing the resulting
artifacts without needing to mentally manage the jobs. Simply queue the files, then release
them to print as the printer finishes.

### Roadmap / Epics
 * [ ] Append gcode to a queue - v0.1-alpha
 * [ ] Add gcode files with multiplier so they will be printed multiple times - v0.2-alpha
 * [ ] Remove gcode files from queue - v0.3-alpha
 * [ ] Integration testing framework using Docker to emulate octoprint - v0.4-alpha
 * [ ] Release gcode files to an octoprint server - v1.0, minimum viable product
 * [ ] Ability to edit jobs once they have been added to the queue, e.g. to change multiples - v1.1
 * [ ] Ability to queue files with 'capability' tags which indicate what kind of printer they should be released to - v2.0
 * [ ] Ability to preconfigure multiple printer servers with capability tags to determine what kinds of jobs they should receive - v2.0
 * [ ] Instead of releasing jobs directly, allow operator to mark printers as ready to print after manually clearing, job release happens automatically when printer marked as ready - v2.0
 * [ ] Support for printers running Moonraker API - v2.1
 * [ ] Integrate Slicer engine to allow queueing of STL files directly - v2.2
 * [ ] Preconfigure slicer profiles which automatically add capability tags to their generated jobs - v2.2
 * [ ] Web Service which emulates Octoprint endpoints to allow for gcode upload directly from Slicer - v3
 * [ ] Kanban board to tie printable artifacts to larger builds and projects - v3
