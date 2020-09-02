
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { PasswordValidation } from './password-validation';
// declare var $;
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  myForm: FormGroup;
  email: string = "";
  firstName: string = "";
  lastName: string = "";
  address: string = "";
  phone: number;
  //    password: '',
  //    confirmPassword: '',

  constructor( private formBuilder: FormBuilder) { }

  ngOnInit() {

    this.myForm = this.formBuilder.group({
      email: new FormControl('', [Validators.required, Validators.email]),
      firstName: new FormControl('', [Validators.required, Validators.minLength(2), Validators.maxLength(50), Validators.pattern('^[a-zA-Z \-\']+')]),
      lastName: new FormControl('', [Validators.required, Validators.minLength(2), Validators.maxLength(50), Validators.pattern('^[a-zA-Z \-\']+')]),
      address: new FormControl('', [Validators.maxLength(255)]),
      phone: new FormControl('', [Validators.required, Validators.minLength(10), Validators.maxLength(11)]),
      password: new FormControl('', [Validators.required, Validators.maxLength(20)]),
      confirmPassword: new FormControl('', [Validators.required, Validators.maxLength(20)])
    },
      {
        validator: PasswordValidation.MatchPassword
      })
  }

  onSubmit() {
    const request = {
      email: this.myForm.value.email,
    }
   
    //  console.log(this.myForm)
    //  localStorage.setItem('registration', this.myForm.value.email);
  }
  reset() {
    this.myForm.reset();
  }
  restrictNumeric(e) {
    if ((e.keyCode >= 48 && e.keyCode <= 57) || (e.keyCode >= 96 && e.keyCode <= 105)) {
      e.preventDefault();
    }
  }
  restrictAlpha(e) {
    if (((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) && e.keyCode != 8) {
      e.preventDefault();
    }
  }
}

