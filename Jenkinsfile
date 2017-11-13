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
ld -o totp totp.o sha1.o'''
      }
    }
    stage('Run') {
      steps {
        sh '''cd tests/c/totp
./totp'''
      }
    }
    stage('error') {
      steps {
        echo 'Done!'
      }
    }
  }
}