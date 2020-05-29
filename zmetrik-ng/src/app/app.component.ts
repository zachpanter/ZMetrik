import {MenuItem} from 'primeng/api';

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'zmetrik-ng';

  items: MenuItem[];

  ngOnInit() {
      this.items = [
          {label: 'Nahrung', icon: 'pi pi-fw pi-home'},
          {label: 'Morphometrik', icon: 'pi pi-fw pi-calendar'},
          {label: 'Rauminhalt', icon: 'pi pi-fw pi-pencil'},
          {label: 'Settings', icon: 'pi pi-fw pi-cog'}
      ];
  }
}