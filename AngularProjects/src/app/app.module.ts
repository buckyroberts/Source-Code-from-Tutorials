import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {  ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { RegisterComponent } from './register/register.component';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    RegisterComponent,
    HomePageComponent,
  ],
  imports : [
    BrowserModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      {path:'',component:LoginPageComponent},
      {path:'register',component:RegisterComponent},
      {path: 'home-page',component:HomePageComponent},
    ])
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
