document.addEventListener("DOMContentLoaded", function () {
	const profileContainer = document.querySelector(".group");
	const fileInput = document.getElementById("file-input");
	const modal = document.getElementById("upload-modal");
	const dropZone = document.getElementById("drop-zone");
	const browseBtn = document.getElementById("browse-btn");
	const cancelBtn = document.getElementById("cancel-btn");
	const uploadBtn = document.getElementById("upload-btn");
	const imagePreview = document.getElementById("image-preview");
	const previewImage = document.getElementById("preview-image");
	const profilePicture = document.getElementById("profile-picture");

	let selectedFile = null;

	// Open modal when clicking on profile picture
	profileContainer.addEventListener("click", () => {
		modal.classList.remove("hidden");
	});

	// Browse files button
	browseBtn.addEventListener("click", () => {
		fileInput.click();
	});

	// File input change
	fileInput.addEventListener("change", (e) => {
		if (e.target.files.length) {
			handleFileSelection(e.target.files[0]);
		}
	});

	// Drag and drop
	["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
		dropZone.addEventListener(eventName, preventDefaults, false);
	});

	function preventDefaults(e) {
		e.preventDefault();
		e.stopPropagation();
	}

	["dragenter", "dragover"].forEach((eventName) => {
		dropZone.addEventListener(eventName, highlight, false);
	});

	["dragleave", "drop"].forEach((eventName) => {
		dropZone.addEventListener(eventName, unhighlight, false);
	});

	function highlight() {
		dropZone.classList.add("border-blue-500", "bg-blue-50");
	}

	function unhighlight() {
		dropZone.classList.remove("border-blue-500", "bg-blue-50");
	}

	dropZone.addEventListener("drop", (e) => {
		const dt = e.dataTransfer;
		const file = dt.files[0];
		if (file && file.type.match("image.*")) {
			handleFileSelection(file);
		}
	});

	// Handle file selection
	function handleFileSelection(file) {
		selectedFile = file;

		// Show preview
		const reader = new FileReader();
		reader.onload = (e) => {
			previewImage.src = e.target.result;
			imagePreview.classList.remove("hidden");
			uploadBtn.disabled = false;
		};
		reader.readAsDataURL(file);
	}

	// Cancel button
	cancelBtn.addEventListener("click", () => {
		modal.classList.add("hidden");
		resetModal();
	});

	// Upload button
	uploadBtn.addEventListener("click", () => {
		if (selectedFile) {
			// Here you would typically upload the file to your server
			// For demo, we'll just update the profile picture
			const reader = new FileReader();
			reader.onload = (e) => {
				profilePicture.src = e.target.result;
				modal.classList.add("hidden");
				resetModal();
			};
			reader.readAsDataURL(selectedFile);
		}
	});

	// Reset modal state
	function resetModal() {
		selectedFile = null;
		fileInput.value = "";
		imagePreview.classList.add("hidden");
		uploadBtn.disabled = true;
		unhighlight();
	}
});
