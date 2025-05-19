import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzButtonModule } from 'ng-zorro-antd/button';

@Component({
  selector: 'app-management-home',
  imports: [CommonModule , NzLayoutModule, NzButtonModule],
  templateUrl: './management-home.component.html',
  styleUrl: './management-home.component.css'
})
export class ManagementHomeComponent {

  openAlumnimanagement(){
    console.log("Opening Alumni Management");
    location.href = "/alumnimanagement";
  }

  openCompanymanagement(){
    console.log("Opening Company Management");
    location.href = "/companymanagement";
  }

}
