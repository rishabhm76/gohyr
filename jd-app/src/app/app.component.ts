import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'jd-app';
  jdFile!: File;
  resumeFile!: File;
  baseApiUrl: string = ''; //'http://localhost:5000/upload/';
  response!: string;

  constructor(public http: HttpClient) {
    this.http.get('assets/config.json').subscribe((res: any)=>{
      this.baseApiUrl = res.api.upload;
    })
   }

  onChangeJd($event: any) {
    this.jdFile = $event.target.files[0];
  }
  onChangeResume($event: any) {
    this.resumeFile = $event.target.files[0];
  }
  onUpload() {

    // Create form data
    const formData = new FormData();
    
    // Store form name as "file" with file data
    formData.append("jdFile", this.jdFile, this.jdFile.name);
    formData.append("resumeFile", this.resumeFile, this.resumeFile.name);

    // Make http post request over api
    // with formData as req
    this.http.post(this.baseApiUrl, formData).subscribe((res: any) => {
      console.log(res);
      this.response = JSON.stringify(res);
    }, (er: any) => {
      this.response = JSON.stringify(er);
    });
  }
}
