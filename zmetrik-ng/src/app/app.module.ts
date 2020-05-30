import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {TabMenuModule} from 'primeng/tabmenu';
import { MorphometriksComponent } from './morphometriks/morphometriks.component';
import { NahrungComponent } from './nahrung/nahrung.component';
import { RauminhaltComponent } from './rauminhalt/rauminhalt.component';

@NgModule({
  declarations: [
    AppComponent,
    MorphometriksComponent,
    NahrungComponent,
    RauminhaltComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    TabMenuModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
