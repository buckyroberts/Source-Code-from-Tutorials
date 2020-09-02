
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

 
@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  registerForm: FormGroup;
  submitted = false;
 
  constructor(private formBuilder: FormBuilder) { }
 
  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      username: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }
 
  get f() {
    return this.registerForm.controls;
  }
 
  onSubmit() {
    this.submitted = true;
 
    if (this.registerForm.invalid) {
      return;
    }
 
    console.log('email=' + this.f.email.value);
    console.log('username=' + this.f.username.value);
    console.log('password=' + this.f.password.value);
  }
}