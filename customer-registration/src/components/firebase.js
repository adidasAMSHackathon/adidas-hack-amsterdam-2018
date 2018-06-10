import firebase from 'firebase'

const firebaseApp = firebase.initializeApp({
  apiKey: 'AIzaSyB7-KGtvRMMdqBHCLCHPRCbNHHSoZ4AcVM',
  authDomain: 'adidas-hack-amsterdam-2018.firebaseapp.com',
  databaseURL: 'https://adidas-hack-amsterdam-2018.firebaseio.com',
  projectId: 'adidas-hack-amsterdam-2018',
  storageBucket: 'adidas-hack-amsterdam-2018.appspot.com',
  messagingSenderId: '762733776336'
})

export const storageReferences = {
  'db': firebaseApp.database(),
  'storage': firebaseApp.storage()
}
