"""
Neural Network for Solar Panel Segmentation
that handles 3-channel images by subtracting
a channel from a 4-channel img
"""

if __name__ == '__main__':
    # Import(s)
    import os
    from pathlib import Path
    import nn_lib
    # from pytorch_lightning.callbacks import ModelCheckpoint # For loading checkpoints

    # Current working directory
    cwd = Path.cwd()
    parent = cwd.parent

    # Root path to the dataset
    DATA_DIR = os.path.join(parent, "NN Prepare", "NY-Q", "tiles")

    # File with the list of images to use for testing, training, and validation
    test = os.path.join(DATA_DIR, 'test_2024.txt')
    train = os.path.join(DATA_DIR, 'train_2024.txt')
    validate = os.path.join(DATA_DIR, 'val_2024.txt')

    # # File for checkpoint (found in this dir, not NN Prepare)
    # check_point_file = os.path.join(".", 'lightning_logs', 'version_2', 'checkpoints', 'epoch=9-step=600.ckpt')

    # Size to crop the images during augmentation
    CROPSIZE = 576  # Must be divisible by 32

    # Some training hyperparameters
    BATCH_SIZE = 2
    EPOCHS = 6

    # Channel variable (channel to delete ['R', 'G', 'B', 'A'])
    channel = -4

    # Img ending
    img = "jp2"

    # Img Type
    img_type = "RGBA"

    # Create datasets, dataloaders, and other necessary objects
    train_loader, valid_loader, test_loader, T_MAX, OUT_CLASSES = nn_lib.create_objs(DATA_DIR, img, train, validate, test, CROPSIZE, BATCH_SIZE, EPOCHS, img_type, channel)

    # Models
    # # Model for Training 1
    model = nn_lib.SolarModel("FPN", "resnext50_32x4d", in_channels=3, out_classes=OUT_CLASSES, t_max=T_MAX)
    # # Model for Training 2
    # model = nn_lib.SolarModel("FPN", "mit_b0", in_channels=3, out_classes=OUT_CLASSES, t_max=T_MAX)
    # # Model for Trained Checkpoint 1
    # model = nn_lib.SolarModel.load_from_checkpoint(check_point_file, arch="FPN", encoder_name="resnext50_32x4d", in_channels=3,
    #                                         out_classes=OUT_CLASSES, t_max=T_MAX)
    # # Model for Trained Checkpoint 2
    # model = nn_lib.SolarModel.load_from_checkpoint(check_point_file, arch="FPN", encoder_name="mit_b0", in_channels=3,
    #                                         out_classes=OUT_CLASSES, t_max=T_MAX)

    # # Load checkpoint
    # checkpoint_callback = ModelCheckpoint(
    #     filename=check_point_file,
    #     save_top_k=1,
    #     mode='max'
    # )

    # Show output
    nn_lib.output(EPOCHS, model, train_loader, valid_loader, test_loader)