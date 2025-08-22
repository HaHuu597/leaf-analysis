document.addEventListener("DOMContentLoaded", () => {
  const startBtn = document.getElementById("startCamera");
  const video = document.getElementById("camera");
  const captureBtn = document.getElementById("captureBtn");
  const hiddenInput = document.getElementById("capturedImage");

  // Bấm nút mở camera
  if (startBtn) {
    startBtn.addEventListener("click", () => {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            video.style.display = "block";
            captureBtn.style.display = "inline-block";
            startBtn.style.display = "none"; // ẩn nút mở camera
            video.srcObject = stream;
          })
          .catch(err => {
            alert("Không mở được camera: " + err);
            console.error("❌ Lỗi camera:", err);
          });
      } else {
        alert("Trình duyệt không hỗ trợ camera API.");
      }
    });
  }

  // Bấm chụp ảnh
  if (captureBtn) {
    captureBtn.addEventListener("click", () => {
      const canvas = document.getElementById("canvas");
      const ctx = canvas.getContext("2d");
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Chuyển sang base64
      const dataURL = canvas.toDataURL("image/png");
      hiddenInput.value = dataURL;

      alert("Ảnh đã chụp, bấm 'Dự đoán ảnh chụp' để gửi!");
    });
  }
});


// // Hiển thị tên file khi chọn ảnh
// document.addEventListener("DOMContentLoaded", () => {
//   const input = document.getElementById("imageInput");
//   if (input) {
//     input.addEventListener("change", () => {
//       if (input.files.length > 0) {
//         alert("Đã chọn ảnh: " + input.files[0].name);
//       }
//     });
//   }
// });
// Hiển thị tên file khi chọn ảnh==================

// document.addEventListener("DOMContentLoaded", () => {
//   const startBtn = document.getElementById("startCamera");
//   const video = document.getElementById("camera");
//   const captureBtn = document.getElementById("captureBtn");

//   if (startBtn) {
//     startBtn.addEventListener("click", () => {
//       navigator.mediaDevices.getUserMedia({ video: true })
//         .then(stream => {
//           video.style.display = "block";
//           captureBtn.style.display = "inline-block";
//           startBtn.style.display = "none"; // ẩn nút mở camera
//           video.srcObject = stream;
//         })
//         .catch(err => console.error("❌ Không mở được camera:", err));
//     });
//   }

//   if (captureBtn) {
//     captureBtn.addEventListener("click", () => {
//       const canvas = document.getElementById("canvas");
//       const ctx = canvas.getContext("2d");
//       canvas.width = video.videoWidth;
//       canvas.height = video.videoHeight;
//       ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

//       const dataURL = canvas.toDataURL("image/png");
//       document.getElementById("capturedImage").value = dataURL;

//       alert("Ảnh đã được chụp, bấm 'Dự đoán ảnh chụp' để gửi!");
//     });
//   }
// });

// document.addEventListener("DOMContentLoaded", () => {====================
//   const input = document.getElementById("imageInput");
//   if (input) {
//     input.addEventListener("change", () => {
//       if (input.files.length > 0) {
//         alert("Đã chọn ảnh: " + input.files[0].name);
//       }
//     });
//   }

//   // Khởi động camera
//   const video = document.getElementById("camera");
//   if (video) {
//     navigator.mediaDevices.getUserMedia({ video: true })
//       .then(stream => { video.srcObject = stream; })
//       .catch(err => console.error("Không mở được camera:", err));
//   }

//   // Chụp ảnh từ video
//   const captureBtn = document.getElementById("captureBtn");
//   if (captureBtn) {
//     captureBtn.addEventListener("click", () => {
//       const canvas = document.getElementById("canvas");
//       const ctx = canvas.getContext("2d");
//       canvas.width = video.videoWidth;
//       canvas.height = video.videoHeight;
//       ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

//       // Chuyển ảnh sang base64 để gửi lên server
//       const dataURL = canvas.toDataURL("image/png");
//       document.getElementById("capturedImage").value = dataURL;

//       alert("Ảnh đã được chụp, bấm 'Dự đoán ảnh chụp' để gửi!");
//     });
//   }
// });
