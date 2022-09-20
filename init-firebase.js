import { initializeApp } from 'firebase/app';
import { getFirestore, collection, getDocs } from 'firebase/firestore/lite';

const firebaseConfig = {
  apiKey: "AIzaSyDUzrNuvxFeRmKWSSxUafrewdvbStKrBkY",
  authDomain: "sw-mini-project-362120.firebaseapp.com",
  projectId: "sw-mini-project-362120",
  storageBucket: "sw-mini-project-362120.appspot.com",
  messagingSenderId: "88132589730",
  appId: "1:88132589730:web:48e51242a3f89a39711ffb",
  measurementId: "G-J3G3B9QSDN"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);