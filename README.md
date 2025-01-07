# Int_Artificial
Aquí se almacenarán todos los trabajos del curso.


cudatoolkit - nvidia driver - nvidia container
I selected the Method 1 of my findings below, which is:
    sudo vim /etc/nvidia-container-runtime/config.toml, then changed no-cgroups = false, save
    Restart docker daemon: sudo systemctl restart docker, then you can test by running sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi 
