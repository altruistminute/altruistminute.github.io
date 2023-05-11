// Initialize Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.21.0/firebase-auth.js";

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB_9WU3QkXteKS5CV2LXxjvRpJRUrXgXHI",
  authDomain: "melindacorp-9d026.firebaseapp.com",
  projectId: "melindacorp-9d026",
  storageBucket: "melindacorp-9d026.appspot.com",
  messagingSenderId: "274357860166",
  appId: "1:274357860166:web:0142ec8ea45a14706d5747",
  measurementId: "G-ZJZL050VN0"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth();

const email = document.getElementById('email');
const password = document.getElementById('password');
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
const messageDiv = document.getElementById('message');

// Add login event
loginForm.addEventListener('submit', e => {


	// Get user info
	const userEmail = email.value;
	const userPassword = password.value;

	// Sign in
	auth.signInWithEmailAndPassword(userEmail, userPassword)
		.then(userCredential => {
			// Do something on successful login
			console.log(userCredential);
		})
		.catch(error => {
			// Handle login error
			console.log(error);
		});
});

// Add signup event
signupForm.addEventListener('submit', e => {


	// Get user info
	const userEmail = email.value;
	const userPassword = password.value;

	auth.createUserWithEmailAndPassword(userEmail, userPassword)
		.then(userCredential => {
			// Do something on successful signup
			console.log(userCredential);
		})
		.catch(error => {
			// Handle signup error
			console.log(error);
		});
});
