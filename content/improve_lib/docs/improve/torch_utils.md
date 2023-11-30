Module improve.torch_utils
==========================

Classes
-------

`TestbedDataset(root='/tmp', dataset='davis', xd=None, xt=None, y=None, transform=None, pre_transform=None, smile_graph=None, saliency_map=False)`
:   Dataset base class for creating graph datasets which easily fit
    into CPU memory.
    Inherits from :class:`torch_geometric.data.Dataset`.
    See `here <https://pytorch-geometric.readthedocs.io/en/latest/notes/
    create_dataset.html#creating-in-memory-datasets>`__ for the accompanying
    tutorial.
    
    Args:
        root (string, optional): Root directory where the dataset should be
            saved. (default: :obj:`None`)
        transform (callable, optional): A function/transform that takes in an
            :obj:`torch_geometric.data.Data` object and returns a transformed
            version. The data object will be transformed before every access.
            (default: :obj:`None`)
        pre_transform (callable, optional): A function/transform that takes in
            an :obj:`torch_geometric.data.Data` object and returns a
            transformed version. The data object will be transformed before
            being saved to disk. (default: :obj:`None`)
        pre_filter (callable, optional): A function that takes in an
            :obj:`torch_geometric.data.Data` object and returns a boolean
            value, indicating whether the data object should be included in the
            final dataset. (default: :obj:`None`)

    ### Ancestors (in MRO)

    * torch_geometric.data.in_memory_dataset.InMemoryDataset
    * torch_geometric.data.dataset.Dataset
    * torch.utils.data.dataset.Dataset
    * typing.Generic

    ### Instance variables

    `processed_file_names`
    :   The name of the files in the :obj:`self.processed_dir` folder that
        must be present in order to skip processing.

    `raw_file_names`
    :   The name of the files in the :obj:`self.raw_dir` folder that must
        be present in order to skip downloading.

    ### Methods

    `download(self)`
    :   Downloads the dataset to the :obj:`self.raw_dir` folder.

    `getXD(self)`
    :

    `process(self, xd, xt, y, smile_graph)`
    :   Processes the dataset to the :obj:`self.processed_dir` folder.