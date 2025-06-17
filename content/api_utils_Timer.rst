Timer
-----------------------------------------

:funcelse:`class improvelib.utils.Timer()`

Measures time.

Used in *preprocess*, *train*, and *infer*. Also used in workflows.

.. container:: utilhead:
  
  Attributes:

**start** : Time
  Time at init (start).

**end** : Time
  Time when timer_end() is called.

**time_diff** : Time
  Difference in time between :code:`start` and :code:`end` in seconds.

**hours** : int
  Hours in :code:`time_diff`, when converted to HH:MM:SS.

**minutes** : int
  Minutes in :code:`time_diff`, when converted to HH:MM:SS. Not total minutes.

**seconds** : int
  Seconds in :code:`time_diff`, when converted to HH:MM:SS. Not total seconds.

**time_diff_dict** : dict
  Dictionary with keys 'hours', 'minutes', 'seconds' to express total time elapsed.

:funcname:`timer_end()`

  Sets attributes :code:`end`, :code:`time_diff`, :code:`hours`, :code:`minutes`, :code:`seconds`, :code:`time_diff_dict`.

  .. container:: utilhead:
  
    Parameters:

  None

  .. container:: utilhead:
  
    Returns:

  None

:funcname:`display_timer()`

  Calls :code:`timer_end`, then both prints and returns the :code:`time_diff_dict`.

  .. container:: utilhead:
  
    Parameters:

  None

  .. container:: utilhead:
  
    Returns:

  **time_diff_dict** : dict
    Dictionary with keys 'hours', 'minutes', 'seconds' to express total time elapsed.


:funcname:`save_timer()`

  Ends timer if needed and saves the timer as a JSON file. Additional items can also be saved if passed.

  .. container:: utilhead:
  
    Parameters:

  **dir_to_save** : str, Path
    Directory to save the JSON file.

  **filename** : str, optional
    Name of the JSON file, including the '.json'. Defaults to 'runtime.json'.

  **extra_dict** : dict, optional
    Dictionary to append to the :code:`time_diff_dict` before saving the file.


  .. container:: utilhead:
  
    Returns:

  **True** : bool


.. container:: utilhead:
  
  Example

The :code:`Timer` should be started in :code:`main()` before the call to :code:`run()` and saved after, as follows:

.. code-block::
  
    timer_preprocess = frm.Timer()
    ml_data_outdir = run(params)
    timer_preprocess.save_timer(dir_to_save=params["output_dir"], 
                                filename='runtime_preprocess.json', 
                                extra_dict={"stage": "preprocess"})
