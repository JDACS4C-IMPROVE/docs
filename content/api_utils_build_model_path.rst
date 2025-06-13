build_model_path
-----------------------------------------

:funcelse:`improvelib.utils.`:funcname:`build_model_path`:funcelse:`(model_file_name, model_file_format, model_dir)`


Returns the path to save/load the trained model.

Used in *train* and *infer*.

.. container:: utilhead:
  
  Parameters:

**model_file_name** : str
  Name of model file

**model_file_format** : str 
  Type of file for model (e.g. '.pt')

**model dir** : Path or str
  Directory path to save the model

.. container:: utilhead:
  
  Returns:

**model_path** : pathlib.Path
  Path to model

.. container:: utilhead:
  
  Example
  
Creates a model path to save the model.
   
.. code-block::

  modelpath = frm.build_model_path(model_file_name=params["model_file_name"],
                                model_file_format=params["model_file_format"],
                                model_dir=params["output_dir"])
  model.save_model(str(modelpath))