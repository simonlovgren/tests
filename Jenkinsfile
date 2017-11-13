pipeline {
  agent any
  stages {
    stage('Sha1 build') {
      steps {
        sh '''pwd
ls
cd c/totp
gcc -c -o sha1.o sha1.c
gcc -c -o totp.o totp.c
gcc -o totp totp.o sha1.o'''
      }
    }
    stage('Run') {
      steps {
        sh '''cd c/totp
./totp "hello world" 11
shasum -a 1 <<< "hello world"'''
      }
    }
  }
}