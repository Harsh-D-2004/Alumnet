import { Component, ViewChild, ElementRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzIconModule } from 'ng-zorro-antd/icon';
import axios from 'axios';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule, 
    NzButtonModule,
    NzInputModule,
    NzLayoutModule,
    NzIconModule
  ],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent {
  @ViewChild('chatMessages') private chatMessagesContainer!: ElementRef;

  messages = [
    { sender: 'bot', text: 'Hello! How can I assist you today?' }
  ];

  userInput = '';
  response = [];
  loading = false;

  async sendMessage() {
    if (!this.userInput.trim()) return;

    this.messages.push({ sender: 'user', text: this.userInput });
    const userQuery = this.userInput;
    this.userInput = '';

    this.scrollToBottom();

    this.loading = true;

    try {
      const response = await axios.post('http://localhost:8000/ask/query', {
        query: userQuery
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const botReply = response.data.result;
      console.log(botReply);
      console.log(response.data);

      this.messages.push({ sender: 'bot', text: botReply });
      this.scrollToBottom();

    } catch (error) {
      console.error('Error sending message:', error);
      this.messages.push({ sender: 'bot', text: 'Sorry, something went wrong.' });
      this.scrollToBottom();
    }
    finally{
      this.loading = false;
      this.scrollToBottom();
    }
  }

  private scrollToBottom() {
    setTimeout(() => {
      this.chatMessagesContainer.nativeElement.scrollTop = this.chatMessagesContainer.nativeElement.scrollHeight;
    }, 100);
  }

  openManagement() {
    console.log('Opening management');
    location.href = "/management";
  }
}
