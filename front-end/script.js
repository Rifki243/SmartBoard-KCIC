const video = document.getElementById('video');
const captureButton = document.getElementById('capture');
const uploadInput = document.getElementById('upload');
const resultDiv = document.getElementById('result');
const uploadButton = document.getElementById('upload-btn'); // Tambahkan referensi ke tombol upload

// Akses kamera
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    });

// Tangkap gambar dari video
captureButton.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0);
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('file', blob, 'image.jpg');  // Pastikan nama file sesuai

        // Mengirim gambar ke endpoint capture-frame
        fetch('/capture-frame/', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            resultDiv.innerHTML = `Nama: ${data.name}, Tiket: ${data.ticket}, Jadwal: ${data.schedule}, Pesan: ${data.message}`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = 'Terjadi kesalahan saat mengupload gambar.';
        });
    });
});

// Mengupload foto manual
uploadInput.addEventListener('change', () => {
    const file = uploadInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // Menampilkan tombol upload untuk konfirmasi
    uploadButton.style.display = 'block'; // Tampilkan tombol upload
});

// Mengupload gambar ketika tombol upload ditekan
uploadButton.addEventListener('click', () => {
    const file = uploadInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload-photo/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        resultDiv.innerHTML = `Nama: ${data.name}, Tiket: ${data.ticket}, Jadwal: ${data.schedule}, Pesan: ${data.message}`;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = 'Terjadi kesalahan saat mengupload gambar.';
    });
});
