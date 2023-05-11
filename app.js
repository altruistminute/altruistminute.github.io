// Initialize Firebase
var firebaseConfig = {
	apiKey: "YOUR_API_KEY",
	authDomain: "YOUR_AUTH_DOMAIN",
	projectId: "YOUR_PROJECT_ID",
	storageBucket: "YOUR_STORAGE_BUCKET",
	messagingSenderId: "YOUR_SENDER_ID",
	appId: "YOUR_APP_ID"
};

firebase.initializeApp(firebaseConfig);

// Get elements
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const signupForm = document.getElementById('signup-form');
const messageDiv = document.getElementById('message');

// Add signup event
signupForm.addEventListener('submit', e => {
	e.preventDefault(); // Prevent form from submitting

	// Get user info
	const email = emailInput.value;
	const password = passwordInput.value;
	const confirmPassword = confirmPasswordInput.value;

	if (password !== confirmPassword) {
		messageDiv.innerHTML = 'Les mots de passe ne correspondent pas';
		messageDiv.style.color = 'red';
		return;
	}

	// Sign up
	firebase.auth().createUserWithEmailAndPassword(email, password)
		.then(() => {
			messageDiv.innerHTML = 'Compte créé avec succès!';
			messageDiv.style.color = 'green';
		})
		.catch(error => {
			messageDiv.innerHTML = error.message;
			messageDiv.style.color = 'red';
		});
});
