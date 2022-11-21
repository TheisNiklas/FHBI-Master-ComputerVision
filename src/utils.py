def buildRunName(modelName: str, transferLearning: bool, epoch: int, batchSize: int) -> str:
    """
    Generates the name for the current run

    Args:
        modelName (str): Name of the used base model
        transferLearning (bool): Whether the current run uses transfer learning
        epoch (int): The total count of epochs
        batchSize (int): The batch size used

    Returns:
        str: The generated run name
    """
    tempStr = modelName
    if transferLearning:
        tempStr += "_transfer"
    else:
        tempStr += "_scratch"
    tempStr += f'_epochs-{epoch}'
    tempStr += f'_batch-{batchSize}'
    return tempStr