Models
========================

Curated community models
--------------

Curated COMMUNITY model are standardized using CANDLE libraries. A tutorial on how to modify a community model to be CANDLE compliant can be found here https://ecp-candle.github.io/Candle/tutorials/writing_candle_code.html. The candle_lib API documentation can be found here https://ecp-candle.github.io/Candle/candle_lib.

1. Standard candle arguement parser will be used.

   a. CANDLE keywords must be used for command line arguements if one exists.  If you have the Benchmarks repo, they can use them as examples, or run --help. SEE ALSO: https://ecp-candle.github.io/Candle/tutorials/default_parameters.html
   
   b. All model arguements are passed to the model by way of the candle --config_file option. For example:
   
   ```
   cadre_candle.py --config_file some_file_name
   ```
   
   b. Non-standard keywords (meaning not represented in the candle keywords) shall be added to the additional_definitions so that they can be included in that they are properly passed to and parsed by the model.  If these keywords (arguments) are not in additional_definitions they can't be changed from the command line.

2. There must be a data_loader that is implemented by/in <model>.py or uses a candle default data_loader. The name shall conform to CANDLE standards.

3. Models shall use candle checkpointing.

4. There will be a data_loader that is implemented by/in the <model>.py file, or uses a candle default data_loader.

5. This data_loader shall be used to load data for training and inferencing.

6. The naming of the data loader shall conform to a CANDLE standard.



Current Models
--------------

.. toctree::
   :maxdepth: 1

   GraphDRP
   hidra
   igtd
   DeepCDR
   MODEL_NAME
   
GitHub Preparation Template
-------------------------
.. toctree::
   :maxdepth: 1
   
   github-readme-template
