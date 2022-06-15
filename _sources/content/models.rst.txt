Models
========================

Curated community models
--------------

Curated community model are standardized using CANDLE libraries.

1. Standard candle arguement parser will be used.

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
