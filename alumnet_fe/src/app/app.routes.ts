import { Routes } from '@angular/router';
import { ChatComponent } from './chat/chat.component';
import { ManagementHomeComponent } from './management-home/management-home.component';

export const routes: Routes = [
    { path: '', component: ChatComponent },
    { path: 'management', component: ManagementHomeComponent }
];
