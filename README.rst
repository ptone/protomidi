ProtoMIDI - a MIDI library for Python
======================================

A small example (API may change)::

    import time
    import random
    from protomidi.msg import *
    from protomidi.portmidi import Output

    # Play random notes
    out = Output()
    while 1:
        note = random.randrange(128)

        out.send(note_on(note=note, velocity=70))
	time.sleep(0.25)
	out.send(note_off(note=note, velocity=127))

MIDI messages are immutable objects. A new message can be created by
calling an existing message and overriding some of its values::

    >>> from protomidi.msg import note_on
    >>> msg = note_on(note=22, velocity=100)
    >>> msg
    note_on(channel=0, note=22, velocity=100)
    >>> msg(note=60)
    note_on(channel=0, note=60, velocity=100)


Planned features
----------------

(All implemented, but with a lot of testing and fine polishing remaining.)

    - abstract immutable MIDI message objects that are
      easy to work with
    
    - support for all MIDI message types (including sysex)
    
    - parser / serializer (seralizes to bytearray or bytes)
    
    - Input and Output classes for communicating with other MIDI
      programs or devices (portmidi)


Status
------

The library is under development. The code may not be stable and the
API may change.


Known bugs
----------

  - on OS X, portmidi sometimes hangs for a couple of seconds while
    initializing.

  - default input/output doesn't work in Linux. Adding a default
    input/output in the alsa config will probably help. (This is not
    really a bug, but just how ALSA works.)

  - in Linux, I am experiencing occational short lags, as if messages
    are bunched up and then released again. I don't know what causes this,
    but I suspect that another process is sometimes stealing the CPU
    for long enough for this to happen. (Could it be garbage collection?
    I doubt it, but I won't count it out yet.)

Requirements
------------

ProtoMIDI works Python 2.7 and 3.2 (may work with older versions, but I haven't tested this.)

Requires portmidi shared library if you want to use the I/O classes.

I'm using Ubuntu 11.4 and Mac OS Lion, but it should run wherever
there you have Python and a portmidi shared library.


Todo
-----

   - show sysex bytes in hexadecimal? (in __repr__())

   - include some kind of event based scheduler (perhaps based on
     http://github/olemb/gametime)

   - include useful lookup tables or message attributes for common things like
     controller types

   - handle devices that send note_on(velocity=0) instead of note_off() (flag
     for portmidi.Input()?) Perhaps make it an option so you can choose the one you prefer,
     and any data will be converted to that format.


Author: Ole Martin Bjørndalen - ombdalen@gmail.com - http://nerdly.info/ole/

License: MIT

Credits: The Portmidi wrapper is based on Portmidizero by Grant Yoshida.
