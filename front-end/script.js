const video = document.getElementById('video');
const resultDiv = document.getElementById('result');
const overlay = document.getElementById('overlay');
const ctx = overlay.getContext('2d');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;

        setInterval(() => {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const context = canvas.getContext('2d');
            context.drawImage(video, 0, 0);

            canvas.toBlob(blob => {
                const formData = new FormData();
                formData.append('file', blob, 'frame.jpg');

                fetch('/auto-detect/', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    resultDiv.innerHTML = `
                        <p><strong>Nama:</strong> ${data.name}</p>
                        <p><strong>Tiket:</strong> ${data.ticket}</p>
                        <p><strong>Jadwal:</strong> ${data.schedule}</p>
                        <p><strong>Pesan:</strong> ${data.message}</p>
                        <p><strong>Sisa Waktu:</strong> ${data.sisa_waktu}</p>
                    `;

                    ctx.clearRect(0, 0, overlay.width, overlay.height);
                    if (data.box) {
                        const [x, y, w, h] = data.box;
                        ctx.strokeStyle = "lime";
                        ctx.lineWidth = 3;
                        ctx.strokeRect(x, y, w, h);

                        if (data.name && data.name !== "Unknown") {
                            ctx.font = "16px Arial";
                            ctx.fillStyle = "lime";
                            ctx.fillText(data.name, x, y - 10);
                        }
                    }
                })
                .catch(err => {
                    resultDiv.innerHTML = "<p><strong>Gagal mendeteksi wajah.</strong></p>";
                    console.error(err);
                });
            }, 'image/jpeg');
        }, 2000);
    })
    .catch(err => console.error('Gagal akses kamera:', err));
