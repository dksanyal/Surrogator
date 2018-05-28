#Surrogator: Tool to identify open access surrogates of access-restricted scholarly articles.
#Written by TYSS Santosh, NDLI, IIT Kharagpur, India

#This software may be used for non-commercial purposes only.

#We request you to mention the following references in any article that is based on work that uses this tool.

# T. Y. S. S. Santosh, Debarshi Kumar Sanyal, and Plaban Kumar Bhowmick. 2018. Surrogator: Enriching a Digital Library with Open Access Surrogate Resources. In ACM India Joint International Conference on Data Sciences and Management of Data, Demo Track (CoDS-COMAD’18).
# T. Y. S. S. Santosh, Debarshi Kumar Sanyal, Plaban Kumar Bhowmick, and Partha Pratim Das. 2018. Surrogator: A Tool to Enrich a Digital Library with Open Access Surrogate Resources. In Proceedings of ACM/IEEE Joint Conference on Digital Libraries, Poster Track (JCDL’18).

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#N.B. This software has been developed as part of a research project and is likely to contain bugs. We will be delighted to receive your feedback on the software including bug reports and bug fixes.
#N.B. Tested on CentOS Linux release 7.3.1611 (Core), Python 3.6 only 


from importlib import reload
import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup
from collections import Counter
import math
import numpy as np
import re
import webbrowser
import time
from nltk.corpus import stopwords
from nltk import download
from nltk import PorterStemmer


class combodemo(QWidget):
    def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QVBoxLayout()
      layout1 = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("Select Source")
      self.cb.addItem("Google Scholar")
      self.cb.addItems(["NDLI"])
      self.e1 = QLineEdit()
      self.e1.setAlignment(Qt.AlignLeft)
      self.e1.setFont(QFont("Arial",20))
      self.b1 = QPushButton("Go")
      self.b1.setCheckable(True)
      self.str=str(0)
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.e1)
      layout1.addStretch()
      layout1.addWidget(self.cb)
      layout1.addStretch()
      layout1.addWidget(self.b1)
      layout.addLayout(layout1)
      self.listWidget = QListWidget()
      self.listWidget.setVisible(True)
      layout.addWidget(self.listWidget)
      self.b2 = QPushButton("Next")
      self.b2.setCheckable(True)
      self.b2.clicked.connect(self.btn2state)
      layout.addWidget(self.b2)
      
      
      self.setLayout(layout)
      self.setWindowTitle("Surrogator v1.11")
   
    def Clicked(self,item):
        index=self.listWidget.currentRow()
        print(index)
        paper=self.listWidget.currentItem().text()
        paper=str(paper).replace("\t","").strip()
        if (index%4 == 0 ):
           
            try:
                new_dict=self.obtained_dict[paper]
                url=new_dict[str(paper)]
                webbrowser.open(url)
            except:
                
                pass
        
        if (index%4 == 2 ):
            
            if(paper=="CLICK HERE FOR NEAR MATCH" ):
                    
                    new_index=index-2
                    new_paper=self.listWidget.item(new_index).text()
                    start_time = time.time()
                    newlist,newdict=collect_authoridlink(new_paper)
                    timecal=time.time()-start_time
                    timecal="%.2f" % (timecal)
                    print(newlist)
                    print(newdict)
                    print(timecal)
                    if(newdict!={}):
                        self.obtained_dict.update(newdict)
                    
                    self.listWidget.takeItem(index)
                    

                    if(len(newlist)>0):
                        tempdum =QListWidgetItem("Surrogate :   ( time = "+ timecal +" seconds )")
                        tempdum.setFont(QFont('SansSerif', 8))
                        self.listWidget.insertItem(index,tempdum)
                        i=0
                        while(i<len(newlist)):
                            temp4 =QListWidgetItem("")
                            temp4.setFont(QFont('SansSerif',1)) 
                            self.listWidget.insertItem(index+i*4+1,temp4)

                            temp1 =QListWidgetItem('\t'+newlist[i][0])
                            temp1.setForeground(QColor('#1a0dab'))
                            temp1.setFont(QFont('SansSerif', 14)) 
                            self.listWidget.insertItem(index+2+4*i,temp1)
              
                            temp2 =QListWidgetItem('\t'+newlist[i][1])
                            temp2.setForeground(QColor('#006621')) 
                            temp2.setFont(QFont('SansSerif', 10))
                            self.listWidget.insertItem(index+3+4*i,temp2)
              
                            temp3 =QListWidgetItem('\t'+newlist[i][2])
                            temp3.setForeground(QColor('#1a0dab')) 
                            temp3.setFont(QFont('SansSerif', 8))
                            self.listWidget.insertItem(index+4+4*i,temp3)
                            
                               
                            
                            i+=1
                        
                    else:
                         temp1 =QListWidgetItem("No article found.   ( time ="+timecal+" seconds )" )
                   
                         temp1.setFont(QFont('SansSerif', 8)) 
                         self.listWidget.insertItem(index,temp1)
            elif(paper=="CLICK HERE FOR SURROGATES"):
                    new_index=index-2
                    new_paper=self.listWidget.item(new_index).text()
                    new_index2=index-1
                    new_paper1=self.listWidget.item(new_index2).text()
                    start_time = time.time()
                    newlist,newdict=collect_authoridlinkndl(new_paper,new_paper1)
                    timecal=time.time()-start_time
                    timecal="%.2f" % (timecal)
                    print(newlist)
                    print(newdict)
                    print(timecal)
                    if(newdict!={}):
                        self.obtained_dict.update(newdict)
                    
                    self.listWidget.takeItem(index)
                    

                    if(len(newlist)>0):
                        tempdum =QListWidgetItem("Surrogate :   ( time = "+ timecal +" seconds )")
                        tempdum.setFont(QFont('SansSerif', 8))
                        self.listWidget.insertItem(index,tempdum)
                        i=0
                        while(i<len(newlist)):
                            temp4 =QListWidgetItem("")
                            temp4.setFont(QFont('SansSerif',1)) 
                            self.listWidget.insertItem(index+i*4+1,temp4)

                            temp1 =QListWidgetItem('\t'+newlist[i][0])
                            temp1.setForeground(QColor('#1a0dab'))
                            temp1.setFont(QFont('SansSerif', 14)) 
                            self.listWidget.insertItem(index+2+4*i,temp1)
              
                            temp2 =QListWidgetItem('\t'+newlist[i][1])
                            temp2.setForeground(QColor('#006621')) 
                            temp2.setFont(QFont('SansSerif', 10))
                            self.listWidget.insertItem(index+3+4*i,temp2)
              
                            temp3 =QListWidgetItem('\t'+newlist[i][2])
                            temp3.setForeground(QColor('#1a0dab')) 
                            temp3.setFont(QFont('SansSerif', 8))
                            self.listWidget.insertItem(index+4+4*i,temp3)
                            
                               
                            
                            i+=1
                        
                    else:
                         tempdum =QListWidgetItem("No article found.   ( time = "+ timecal +" seconds )")
                         tempdum.setFont(QFont('SansSerif', 8))
                         self.listWidget.insertItem(index,tempdum)
                   
                 
               
              
            else:
                try:
                    new_index=index-2
                    new_paper=self.listWidget.item(new_index).text()
                    new_paper=str(new_paper).replace("\t","").strip()
                    new_dict=self.obtained_dict[new_paper]
                    url=new_dict[str(paper)]
                    webbrowser.open(url)
                except:
                    pass
         
            
          
          
     
      
 
    def btnstate(self):
        if self.b1.isChecked():
            self.listWidget.clear()
            paper=self.e1.text()
            source=self.cb.currentText()
            pageno=self.str
            self.b1.toggle()
            if(len(paper)!=0):
                #print paper
                if(source== "Select Source"):
                    showdialog2()
                elif(source== "Google Scholar"):
                    self.listWidget.setVisible(True)
                    pageno=0
                    self.obtained_list,self.obtained_dict=googlequery(paper,pageno)
                    pageno=int(pageno)+10
                    self.str=str(pageno)
                            
                    j=1
                    i=0
                    while(i<len(self.obtained_list)):
                        if("CITATION" in self.obtained_list[i][0]):
                            temp1 =QListWidgetItem(str(self.obtained_list[i][0]))
                            #temp1.setForeground(QColor('#000000'))  #DKS
                            temp1.setForeground(QColor('#000000'))
                            temp1.setFont(QFont('SansSerif', 14)) 
                        else:
                            temp1 =QListWidgetItem(str(self.obtained_list[i][0]))
                            #temp1.setForeground(QColor('#1a0dab')) #DKS
                            temp1.setForeground(QColor('#1a0dab'))
                            temp1.setFont(QFont('SansSerif', 14)) 
                        
                        self.listWidget.addItem(temp1)
                        temp2 =QListWidgetItem(str(self.obtained_list[i][1]))
                        temp2.setForeground(QColor('#006621')) 
                        temp2.setFont(QFont('SansSerif', 10))
                        self.listWidget.addItem(temp2)
                        
                        if("CITATION" in self.obtained_list[i][0]):
                            temp4 =QListWidgetItem("")
                            temp4.setFont(QFont('SansSerif',12 ))

                        else:
                            if(self.obtained_list[i][2] !=""):
                                temp4 =QListWidgetItem(self.obtained_list[i][2])
                                temp4.setFont(QFont('SansSerif',12 ))
                            else:
                                temp4 =QListWidgetItem("CLICK HERE FOR NEAR MATCH")
                                temp4.setFont(QFont('SansSerif',8 ))
                    
                        temp4.setForeground(QColor('#FF4500')) 
                        
                        self.listWidget.addItem(temp4)
                        
                        temp5 =QListWidgetItem("")
                        temp5.setFont(QFont('SansSerif',5)) 
                        self.listWidget.addItem(temp5)
                        i+=1
                    self.showMaximized()
                    self.listWidget.itemClicked.connect(self.Clicked)
                    
                    
                        
   
                else:
                    self.listWidget.setVisible(True)
                    
                    self.obtained_list,self.obtained_dict=ndlquery(paper,pageno)
                    
                    j=1
                    i=0
                    while(i<len(self.obtained_list)):
                        temp1 =QListWidgetItem(str(self.obtained_list[i][0]))
                        #temp1.setForeground(self, QColor('#1a0dab'))
                        temp1.setForeground(QColor('#1a0dab'))
                        temp1.setFont(QFont('SansSerif', 14)) 
                        self.listWidget.addItem(temp1)

                        temp2 =QListWidgetItem(str(self.obtained_list[i][1]))
                        temp2.setForeground(QColor('#006621')) 
                        temp2.setFont(QFont('SansSerif', 10))
                        self.listWidget.addItem(temp2)
                        
                        temp3 =QListWidgetItem(self.obtained_list[i][2])
                        temp3.setFont(QFont('SansSerif',8 ))
                        temp3.setForeground(QColor('#FF4500')) 
                        self.listWidget.addItem(temp3)

                        temp4 =QListWidgetItem("")
                        temp4.setFont(QFont('SansSerif',5 ))
                        self.listWidget.addItem(temp4)
                        i+=1
                    self.showMaximized()
                    self.listWidget.itemClicked.connect(self.Clicked)


    def btn2state(self):
        if self.b2.isChecked():
            self.listWidget.clear()
            paper=self.e1.text()
            source=self.cb.currentText()
            pageno=self.str
            self.b2.toggle()
            if(len(paper)!=0):
                #print paper
                if(source== "Select Source"):
                    showdialog2()
                elif(source== "Google Scholar"):
                    self.listWidget.setVisible(True)
                    
                    self.obtained_list,self.obtained_dict=googlequery(paper,pageno)
                    pageno=int(pageno)+10
                    self.str=str(pageno)
                            
                    j=1
                    i=0
                    while(i<len(self.obtained_list)):
                        if("CITATION" in self.obtained_list[i][0]):
                            temp1 =QListWidgetItem(str(self.obtained_list[i][0]))
                            temp1.setForeground(QColor('#000000'))
                            temp1.setFont(QFont('SansSerif', 14)) 
                        else:
                            temp1 =QListWidgetItem(str(self.obtained_list[i][0]))
                            temp1.setForeground(QColor('#1a0dab'))
                            temp1.setFont(QFont('SansSerif', 14)) 
                        
                        self.listWidget.addItem(temp1)
                        temp2 =QListWidgetItem(str(self.obtained_list[i][1]))
                        temp2.setForeground(QColor('#006621')) 
                        temp2.setFont(QFont('SansSerif', 10))
                        self.listWidget.addItem(temp2)
                        
                        if("CITATION" in self.obtained_list[i][0]):
                            temp4 =QListWidgetItem("")
                            temp4.setFont(QFont('SansSerif',12 ))

                        else:
                            if(self.obtained_list[i][2] !=""):
                                temp4 =QListWidgetItem(self.obtained_list[i][2])
                                temp4.setFont(QFont('SansSerif',12 ))
                            else:
                                temp4 =QListWidgetItem("CLICK HERE FOR NEAR MATCH")
                                temp4.setFont(QFont('SansSerif',8 ))
                    
                        temp4.setForeground(QColor('#FF4500')) 
                        
                        self.listWidget.addItem(temp4)
                        
                        temp5 =QListWidgetItem("")
                        temp5.setFont(QFont('SansSerif',5)) 
                        self.listWidget.addItem(temp5)
                        i+=1
                    self.showMaximized()
                    self.listWidget.itemClicked.connect(self.Clicked)
                    
                    
                        
   
                else:
                    self.listWidget.setVisible(True)
                    
                    self.obtained_list,self.obtained_dict=ndlquery(paper,pageno)
                   
                            
                    j=1
                    i=0
                    while(i<len(self.obtained_list)):
                        temp1 =QListWidgetItem(str(self.obtained_list[i][0]))
                        temp1.setForeground(QColor('#1a0dab'))
                        temp1.setFont(QFont('SansSerif', 14)) 
                        self.listWidget.addItem(temp1)

                        temp2 =QListWidgetItem(str(self.obtained_list[i][1]))
                        temp2.setForeground(QColor('#006621')) 
                        temp2.setFont(QFont('SansSerif', 10))
                        self.listWidget.addItem(temp2)
                        
                        temp3 =QListWidgetItem(self.obtained_list[i][2])
                        temp3.setFont(QFont('SansSerif',8 ))
                        temp3.setForeground(QColor('#FF4500')) 
                        self.listWidget.addItem(temp3)

                        temp4 =QListWidgetItem("")
                        temp4.setFont(QFont('SansSerif',5 ))
                        self.listWidget.addItem(temp4)
                        i+=1
                    self.showMaximized()
                    self.listWidget.itemClicked.connect(self.Clicked)       
         

def ndlquery(name,pageno):
           
    url="https://ndl.iitkgp.ac.in/result?q={%22t%22:%22search%22,%22k%22:%22"+name+"%22,%22s%22:[%22type=\%22text\%22%22],%22b%22:{%22filters%22:[]}}"
    
    print(url)
    source_code = requests.get(url, verify=False, proxies = {"http": None, "https": None}) #DKS: verify=False
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    data = soup.find_all("div",{"id":"search-result-group","class":"list-group"})
    obtained_list =[]
    obtained_dict={}
    if(len(data)>0):
        everylink=data[0].find_all("div",{"class":"list-group-item rows"})
        if(len(everylink)>0):
            for i in range(0,len(everylink)):
                eachone_list=[]
                eachone_dict={}
                everyblock=everylink[i].find_all("div",{"class":"col-md-11 col-sm-12"})
                unit_link=""
                unit_name=""
                details=""
                access=""
                if(len(everyblock)>0):
                    heading=everyblock[0].find_all("h4",{"class":"list-group-item-heading overflow-off"})
                    if(len(heading)>0):
                        unitlinklist=heading[0].find_all("a")
                        
                        if(len(unitlinklist)>0):
                            unit_link=unitlinklist[0].get("href")
                            unit_name=unitlinklist[0].contents[0]
                    infoblock=everyblock[0].find_all("div",{"class":"col-sm-5"})
                    if(len(infoblock)>0):
                        authorsinfo=infoblock[0].find_all("div",{"class":"doc-author overflow-off"})
                        if(len(authorsinfo)>0):
                            authorsnames=authorsinfo[0].text
                            details=details+""+authorsnames
                        sourceinfo=infoblock[0].find_all("div",{"class":"text-primary doc-source overflow-off"}) 
                        if(len(sourceinfo)>0):
                            sourcenames=sourceinfo[0].text
                            sourcenames=sourcenames.replace('\n', '')
                            details=details+"::"+sourcenames
                        accessblock= infoblock[0].find_all("div",{"class":"icons"})
                        if(len(accessblock)>0):
                            accessinfo=accessblock[0].find_all("i")
                            if(len(accessinfo)>0):
                                access=accessinfo[0].get("title").replace("/n","")
                        if(access=="Subscribed"):
                            access="CLICK HERE FOR SURROGATES"
                        else:
                            access="Content free in NDLI"
                if(unit_link !=""):
                    eachone_dict[unit_name]=unit_link
                    if(access!="CLICK HERE FOR SURROGATES"):
                        eachone_dict[access]=unit_link
                eachone_list.append(unit_name)
                eachone_list.append(details)
                eachone_list.append(access)
                
                obtained_list.append(eachone_list)
                
                
                if(eachone_dict != {}):
                    obtained_dict[unit_name]=eachone_dict       
    
    return (obtained_list,obtained_dict)  

def googlequery(paper,pageno):
    split_array=str(paper).split() 
    text=''
    #print(paper)
    text=split_array[0]
    for i in range(1,len(split_array)):
        text=text+'+'+split_array[i].replace('"', '').replace("'", '')
    print(text)
    url="https://scholar.google.co.in/scholar?start="+str(pageno)+"&hl=en&q="+text+"&as_sdt=0,5"
	
    print(url)
    source_code = requests.get(url,verify=False) #DKS: verify=False
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    data = soup.find_all("div",{"class":"gs_r"})
        
    obtained_list =[]
    obtained_dict={}
    
    if(len(data)>0):
        for i in range(0,len(data)) :
            eachone_list=[]
            eachone_dict={}
            data1 = data[i].find_all("div",{"class":"gs_ggs gs_fl"})
            pdflink=""
            pdftext=""
            if(len(data1)>0):
                pdf=data1[0].find_all("a")
                pdftext=data1[0].text
                if(len(pdf)>0):
                    pdflink=pdf[0].get("href")
            unit_name=""
            unit_link=""    
            
            link = data[i].find_all("div",{"class":"gs_ri"})  
            unit_namelink =  link[0].find_all("h3",{"class":"gs_rt"})  
            if(len(unit_namelink[0].find_all("span",{"class":"gs_ctu"}))>0):
                unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                for i in range(1,len(unit_namelink[0].contents)):
                    try:
                        unit_name=unit_name +unit_namelink[0].contents[i].text
                    except:
                        unit_name=unit_name +unit_namelink[0].contents[i]

                              
            elif(len(unit_namelink[0].find_all("span",{"class":"gs_ctc"}))>0):
                unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                unit_links=unit_namelink[0].find_all("a")
                if(len(unit_links)>0):
                    unit_name=unit_name+unit_links[0].text
            else:
                unit_links=unit_namelink[0].find_all("a")
                if(len(unit_links)>0):
                    unit_name=unit_name+unit_links[0].text
                       
            if(len(unit_namelink)>0):
                 unit_links=unit_namelink[0].find_all("a")
                 if(len(unit_links)>0):
                     unit_link=unit_links[0].get("href")
            #print unit_name
            #print unit_link
        # if(isinstance(unit_name,str)):
        #     unit_name=unit_name.encode('utf8') 
        # if(isinstance(unit_link,str)):
        #     unit_link=unit_link.encode('utf8')
            details=""
            detailslink =  link[0].find_all("div",{"class":"gs_a"})
            if(len(detailslink)>0):
                 details =  detailslink[0].text



            if(unit_link !=""):
                eachone_dict[unit_name]=unit_link
            eachone_list.append(unit_name)
            eachone_list.append(details)
            if(pdflink !=""):
                eachone_dict[pdftext]=pdflink
            eachone_list.append(pdftext)


            #print eachone_dict
            #print eachone_list
            obtained_list.append(eachone_list)
            
                
            if(eachone_dict != {}):
                obtained_dict[unit_name]=eachone_dict
            #print obtained_dict    
       
        
       
        # # if(isinstance(details,str)):
        # #      details=details.encode('utf8') 
        # eachone_list.append(details)
        # citlink =  link[0].find_all("a",{"class":"gs_nph"})
       
        # if(len(citlink)>1):
        #        cited=citlink[-1].text
               
        #        citation="https://scholar.google.co.in/"+citlink[-1].get("href")
        # if(len(citlink)==1):
        #        cited=citlink[0].text
               
        #        citation="https://scholar.google.co.in/"+citlink[0].get("href")
        # # if(isinstance(cited,str)):
        # #     cited=cited.encode('utf8') 
        # # if(isinstance(citation,str)):
        # #     citation=citation.encode('utf8') 
        # if cited.lower().find("cite") != -1:
        #      eachone_dict[cited]=citation
        #      eachone_list.append(cited)
        # else:
            
        #     eachone_list.append("")
          
        # if(isinstance(pdflink,str)):
        #     pdflink=pdflink.encode('utf8') 
        # if(isinstance(pdftext,str)):
        #     pdftext=pdftext.encode('utf8') 
        
            
        
    return (obtained_list,obtained_dict)

   
def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Please enter some text")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def showdialog2():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Please select some source")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

def collect_authoridlink(paper):
    split=str(paper).split() 
    text=""
    #print(paper)

    for i in range(0,len(split)):
        text=text+"+"+split[i].replace('\"','')
    
    surrogates_list=[] 
    surrogates_dict={}  
    url="https://scholar.google.co.in/scholar?hl=en&q="+text+"&btnG="
    
    source_code = requests.get(url, verify=False) #DKS: verify=False
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    dataset = soup.find_all("div",{"class":"gs_r"})
    bottom = soup.find_all("div",{"id":"gs_res_ccl_bot"})
    
    found=0
   
    
    if(len(dataset)>0):
        for i in range(0,len(dataset)) :
           
            data1 = dataset[i].find_all("div",{"class":"gs_ggs gs_fl"})
            pdflink=""
            pdftext=""
            if(len(data1)>0):
                pdf=data1[0].find_all("a")
                pdftext=data1[0].text
                if(len(pdf)>0):
                    pdflink=pdf[0].get("href")

            
            unit_name=""
            unit_link=""    
            link = dataset[i].find_all("div",{"class":"gs_ri"})  
            unit_namelink =  link[0].find_all("h3",{"class":"gs_rt"})  
            if(len(unit_namelink[0].find_all("span",{"class":"gs_ctu"}))>0):
                unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                add_name=""
                for i in range(1,len(unit_namelink[0].contents)):
                    try:
                        add_name=add_name +unit_namelink[0].contents[i].text
                    except:
                        add_name=add_name +unit_namelink[0].contents[i]
                unit_name=unit_name+add_name
                              
            elif(len(unit_namelink[0].find_all("span",{"class":"gs_ctc"}))>0):
                unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                unit_links=unit_namelink[0].find_all("a")
                add_name=""
                if(len(unit_links)>0):
                     add_name=add_name+unit_links[0].text

                unit_name=unit_name+add_name
                
            else:
                unit_links=unit_namelink[0].find_all("a")
                add_name=""
                if(len(unit_links)>0):
                    add_name=add_name+unit_links[0].text
            
                unit_name=unit_name+add_name

            if(len(unit_namelink)>0):
                unit_links=unit_namelink[0].find_all("a")
                if(len(unit_links)>0):
                     unit_link=unit_links[0].get("href")
            print(paper)
            print(add_name)
            if(str(add_name).lower() == str(paper).lower()) :
                details=""
                detailslink =  link[0].find_all("div",{"class":"gs_a"})
                if(len(detailslink)>0):
                    details =  detailslink[0].text
                    pattern=re.compile('\d\d\d\d')
                    yeararr=re.findall(pattern,details)
                    if(len(yeararr)>0):
                        year=yeararr[-1] 
                addinf=details.split('-') 
                authorslist=""
                if(len(addinf)>0):
                    authorslist = addinf[0] 
                authors=authorslist.split(',') 
                for i in range(0,len(authors)):
                    if(isinstance(authors[i],str)):
                        authors[i]=''.join(i for i in authors[i] if ord(i)<128)
                print(year)
                item= link[0].find_all("div",{"class":"gs_fl"})
                if(len(item)>0):
                     citetext=item[0].find_all("a")
                if(len(citetext)>2):
                    citetext=item[0].find_all("a")[2].text
                    citation="https://scholar.google.co.in/"+item[0].find_all("a")[2].get("href")
                    if citetext.lower().find("cited") != -1 or citetext.lower().find("related")!=-1 :
                         print(citetext)
                         print(citation)
                         surrogates_list,surrogates_dict=findincit(citation,paper,authors,year,surrogates_list,surrogates_dict)

                
                item= link[0].find_all("div",{"class":"gs_fl"})
                if(len(item)>0):
                    citetext=item[0].find_all("a")
                    if(len(citetext)>3):
                         relatedtext=item[0].find_all("a")[3].text
                         relatelink="https://scholar.google.co.in/"+item[0].find_all("a")[3].get("href")
                         if relatedtext.lower().find("related") != -1 or relatedtext.lower().find("cited")!=-1:
                            #print relatedtext
                            #print relatelink
                            surrogates_list,surrogates_dict=findincit(relatelink,paper,authors,year,surrogates_list,surrogates_dict)
		
                if(len(surrogates_list)==0):
                    if(len(bottom)>0):
                        bottext=bottom[0].find_all("a")
                        if(len(bottext)>0):
                            botlink="https://scholar.google.co.in/"+bottom[0].find_all("a")[0].get("href")
                            surrogates_list,surrogates_dict=findincit(botlink,paper,authors,year,surrogates_list,surrogates_dict)
		
                       
    return (surrogates_list,surrogates_dict)     



def collect_authoridlinkndl(paper,paper2):
    split=str(paper).split() 
    text=split[0]
    if(len(split)>1):
        for i in range(1,len(split)):
            text=text+"+"+split[i]
    authors=str(paper2).split("::")
    authorstr=""
    if(len(authors)>0):
        dum="Author:"
        if(dum in authors[0]):
            authorsstr=authors[0].replace(dum,"")
    authornames=[]
    abb_authornames=[]
    authornames=authorsstr.split("|")
    
    if(len(authornames)>0):
        for i in range(0,len(authornames)):
            authornames[i]=authornames[i].strip()
            everyname=authornames[i].split(",")
            if(len(everyname)>1):
                authornames[i]=everyname[1].strip()+" "+everyname[0].strip()
    
    if(len(authornames)>0):
        for i in range(0,len(authornames)):
            everyname=re.split('[. -]',authornames[i])
            
            authornames[i]=""
            for j in range(0,len(everyname)):
                authornames[i]=authornames[i].strip()+" "+ everyname[j].strip()
            authornames[i]=authornames[i].strip()
    
    if(len(authornames)>0):
        for i in range(0,len(authornames)):
            abb_authornames.append(authornames[i])          
    if(len(abb_authornames)>0):
        for i in range(0,len(abb_authornames)):
            eachname=abb_authornames[i].split()
            abb_authornames[i]=""
            if(len(eachname)>0):
                for j in range(0,len(eachname)-1):
                    abb_authornames[i]=abb_authornames[i]+eachname[j][0]
            abb_authornames[i]=abb_authornames[i]+" "+eachname[-1]
            abb_authornames[i]=abb_authornames[i].strip()
    print(authornames)
    print(abb_authornames)
    text2=""
    if(len(abb_authornames)>0):
        text2=abb_authornames[0]
        # if(len(abb_authornames)>1):
        #     for i in range(1,len(abb_authornames)):
        #         text2=text2+"+"+abb_authornames[i]
    
    surrogates_list=[] 
    surrogates_dict={}  
    url="https://scholar.google.co.in/scholar?as_q="+text+"&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors="+text2+"&as_publication=&as_ylo=&as_yhi=&hl=en&as_sdt=0%2C5"
    print(url)
    source_code = requests.get(url, verify=False) #DKS: verify=False
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    dataset = soup.find_all("div",{"class":"gs_r"})
    bottom = soup.find_all("div",{"id":"gs_res_ccl_bot"})

    
       
    if(len(dataset)>0):
         for i in range(0,len(dataset)) :
           
            data1 = dataset[i].find_all("div",{"class":"gs_ggs gs_fl"})
            pdflink=""
            pdftext=""
            if(len(data1)>0):
                pdf=data1[0].find_all("a")
                pdftext=data1[0].text
                if(len(pdf)>0):
                    pdflink=pdf[0].get("href")

            
            unit_name=""
            unit_link=""    
            link = dataset[i].find_all("div",{"class":"gs_ri"})  
            unit_namelink =  link[0].find_all("h3",{"class":"gs_rt"})  
            if(len(unit_namelink[0].find_all("span",{"class":"gs_ctu"}))>0):
                unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                add_name=""
                for i in range(1,len(unit_namelink[0].contents)):
                    try:
                        add_name=add_name +unit_namelink[0].contents[i].text
                    except:
                        add_name=add_name +unit_namelink[0].contents[i]
                unit_name=unit_name+add_name
                              
            elif(len(unit_namelink[0].find_all("span",{"class":"gs_ctc"}))>0):
                unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                unit_links=unit_namelink[0].find_all("a")
                add_name=""
                if(len(unit_links)>0):
                     add_name=add_name+unit_links[0].text

                unit_name=unit_name+add_name
                
            else:
                unit_links=unit_namelink[0].find_all("a")
                add_name=""
                if(len(unit_links)>0):
                    add_name=add_name+unit_links[0].text
            
                unit_name=unit_name+add_name

            if(len(unit_namelink)>0):
                unit_links=unit_namelink[0].find_all("a")
                if(len(unit_links)>0):
                     unit_link=unit_links[0].get("href")
            print(paper)
            print(add_name)
            if(str(add_name).lower() == str(paper).lower()) :
                details=""
                detailslink =  link[0].find_all("div",{"class":"gs_a"})
                if(len(detailslink)>0):
                     details =  detailslink[0].text
                     pattern=re.compile('\d\d\d\d')
                     yeararr=re.findall(pattern,details)
                     if(len(yeararr)>0):
                         year=yeararr[-1] 
              
                # addinf=details.split('-') 
                # authorslist=""
                # if(len(addinf)>0):
                #     authorslist = addinf[0] 
                # authors=authorslist.split(',') 
                # for i in range(0,len(authors)):
                #     if(isinstance(authors[i],str)):
                #         authors[i]=''.join(i for i in authors[i] if ord(i)<128)
                
                item= link[0].find_all("div",{"class":"gs_fl"})
                if(len(item)>0):
                     citetext=item[0].find_all("a")
                if(len(citetext)>2):
                    citetext=item[0].find_all("a")[2].text
                    citation="https://scholar.google.co.in/"+item[0].find_all("a")[2].get("href")
                    if citetext.lower().find("cited") != -1 or citetext.lower().find("related"):
                         print(citetext)
                         print(citation)
                         surrogates_list,surrogates_dict=findincit(citation,paper,abb_authornames,year,surrogates_list,surrogates_dict)

                
                item= link[0].find_all("div",{"class":"gs_fl"})
                if(len(item)>0):
                    citetext=item[0].find_all("a")
                    if(len(citetext)>3):
                         relatedtext=item[0].find_all("a")[3].text
                         relatelink="https://scholar.google.co.in/"+item[0].find_all("a")[3].get("href")
                         if relatedtext.lower().find("related") != -1 or relatedtext.lower().find("cited")!=-1:
                            print(relatedtext)
                            print(relatelink)
                            surrogates_list,surrogates_dict=findincit(relatelink,paper,abb_authornames,year,surrogates_list,surrogates_dict)
               
                if(len(surrogates_list)==0):
                    if(len(bottom)>0):
                        bottext=bottom[0].find_all("a")
                        if(len(bottext)>0):
                            botlink="https://scholar.google.co.in/"+bottom[0].find_all("a")[0].get("href")
                            surrogates_list,surrogates_dict=findincit(botlink,paper,abb_authornames,year,surrogates_list,surrogates_dict)
    
    if(len(surrogates_list)==0):
        text2=abb_authornames[0]
        if(len(abb_authornames)>1):
            text2=abb_authornames[1]
        # if(len(abb_authornames)>1):
        #     for i in range(1,len(abb_authornames)):
        #         text2=text2+"+"+abb_authornames[i]
    
        surrogates_list=[] 
        surrogates_dict={}  
        url="https://scholar.google.co.in/scholar?as_q="+text+"&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors="+text2+"&as_publication=&as_ylo=&as_yhi=&hl=en&as_sdt=0%2C5"
        print(url)
        source_code = requests.get(url, verify=False) #DKS: verify=False
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        dataset = soup.find_all("div",{"class":"gs_r"})
        bottom = soup.find_all("div",{"id":"gs_res_ccl_bot"})
    
       
        if(len(dataset)>0):
             for i in range(0,len(dataset)) :
           
                data1 = dataset[i].find_all("div",{"class":"gs_ggs gs_fl"})
                pdflink=""
                pdftext=""
                if(len(data1)>0):
                    pdf=data1[0].find_all("a")
                    pdftext=data1[0].text
                    if(len(pdf)>0):
                        pdflink=pdf[0].get("href")

            
                unit_name=""
                unit_link=""    
                link = dataset[i].find_all("div",{"class":"gs_ri"})  
                unit_namelink =  link[0].find_all("h3",{"class":"gs_rt"})  
                if(len(unit_namelink[0].find_all("span",{"class":"gs_ctu"}))>0):
                    unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                    add_name=""
                    for i in range(1,len(unit_namelink[0].contents)):
                        try:
                            add_name=add_name +unit_namelink[0].contents[i].text
                        except:
                            add_name=add_name +unit_namelink[0].contents[i]
                    unit_name=unit_name+add_name
                              
                elif(len(unit_namelink[0].find_all("span",{"class":"gs_ctc"}))>0):
                    unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                    unit_links=unit_namelink[0].find_all("a")
                    add_name=""
                    if(len(unit_links)>0):
                         add_name=add_name+unit_links[0].text

                    unit_name=unit_name+add_name
                
                else:
                    unit_links=unit_namelink[0].find_all("a")
                    add_name=""
                    if(len(unit_links)>0):
                        add_name=add_name+unit_links[0].text
            
                    unit_name=unit_name+add_name

                if(len(unit_namelink)>0):
                    unit_links=unit_namelink[0].find_all("a")
                    if(len(unit_links)>0):
                         unit_link=unit_links[0].get("href")
                print(paper)
                print(add_name)
                if(str(add_name).lower() == str(paper).lower()) :
                    details=""
                    detailslink =  link[0].find_all("div",{"class":"gs_a"})
                    if(len(detailslink)>0):
                         details =  detailslink[0].text
                         pattern=re.compile('\d\d\d\d')
                         yeararr=re.findall(pattern,details)
                         if(len(yeararr)>0):
                             year=yeararr[-1] 
                    # details=""
                    # detailslink =  link[0].find_all("div",{"class":"gs_a"})
                    # if(len(detailslink)>0):
                    #     details =  detailslink[0].text
              
                    # addinf=details.split('-') 
                    # authorslist=""
                    # if(len(addinf)>0):
                    #     authorslist = addinf[0] 
                    # authors=authorslist.split(',') 
                    # for i in range(0,len(authors)):
                    #     if(isinstance(authors[i],str)):
                    #         authors[i]=''.join(i for i in authors[i] if ord(i)<128)
                
                    item= link[0].find_all("div",{"class":"gs_fl"})
                    if(len(item)>0):
                         citetext=item[0].find_all("a")
                    if(len(citetext)>2):
                        citetext=item[0].find_all("a")[2].text
                        citation="https://scholar.google.co.in/"+item[0].find_all("a")[2].get("href")
                        if citetext.lower().find("cited") != -1 or citetext.lower().find("related"):
                            print(citetext)
                            print(citation)
                            surrogates_list,surrogates_dict=findincit(citation,paper,abb_authornames,year,surrogates_list,surrogates_dict)

                    item= link[0].find_all("div",{"class":"gs_fl"})
                    if(len(item)>0):
                        citetext=item[0].find_all("a")
                        if(len(citetext)>3):
                            relatedtext=item[0].find_all("a")[3].text
                            relatelink="https://scholar.google.co.in/"+item[0].find_all("a")[3].get("href")
                            if relatedtext.lower().find("related") != -1 or relatedtext.lower().find("cited"):
                              print(relatedtext)
                              print(relatelink)
                              surrogates_list,surrogates_dict=findincit(relatelink,paper,abb_authornames,year,surrogates_list,surrogates_dict)
                       
                    if(len(surrogates_list)==0):
                        if(len(bottom)>0):
                            bottext=bottom[0].find_all("a")
                            if(len(bottext)>0):
                              botlink="https://scholar.google.co.in/"+bottom[0].find_all("a")[0].get("href")
                              surrogates_list,surrogates_dict=findincit(botlink,paper,abb_authornames,year,surrogates_list,surrogates_dict)
    return (surrogates_list,surrogates_dict)     

   
def findincit(url,paper,authors,year,surrogates_list,surrogates_dict):
    
    
    source_code = requests.get(url, verify=False) #DKS: verify=False
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    dataset = soup.find_all("div",{"class":"gs_r"})
    ans=0
    cityear=""
    if(len(dataset)>0):
        for i in range(0,len(dataset)) :
           
            data1 = dataset[i].find_all("div",{"class":"gs_ggs gs_fl"})
            pdflink=""
            pdftext=""
            if(len(data1)>0):
                pdf=data1[0].find_all("a")
                pdftext=data1[0].text
                if(len(pdf)>0):
                    pdflink=pdf[0].get("href")

            if(pdflink!=""):
                unit_name=""
                unit_link=""    
                link = dataset[i].find_all("div",{"class":"gs_ri"})  
                unit_namelink =  link[0].find_all("h3",{"class":"gs_rt"})  
                if(len(unit_namelink[0].find_all("span",{"class":"gs_ctu"}))>0):
                    unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                    add_name=""
                    for i in range(1,len(unit_namelink[0].contents)):
                        try:
                            add_name=add_name +unit_namelink[0].contents[i].text
                        except:
                            add_name=add_name +unit_namelink[0].contents[i]
                    unit_name=unit_name+add_name
                              
                elif(len(unit_namelink[0].find_all("span",{"class":"gs_ctc"}))>0):
                    unit_name=unit_namelink[0].find_all("span",{"class":"gs_ct1"})[0].text
                    unit_links=unit_namelink[0].find_all("a")
                    add_name=""
                    if(len(unit_links)>0):
                         add_name=add_name+unit_links[0].text

                    unit_name=unit_name+add_name
                    
                else:
                    unit_links=unit_namelink[0].find_all("a")
                    add_name=""
                    if(len(unit_links)>0):
                        add_name=add_name+unit_links[0].text
            
                    unit_name=unit_name+add_name

                if(len(unit_namelink)>0):
                    unit_links=unit_namelink[0].find_all("a")
                    if(len(unit_links)>0):
                         unit_link=unit_links[0].get("href")
            
                details=""
                detailslink =  link[0].find_all("div",{"class":"gs_a"})
                if(len(detailslink)>0):
                    details =  detailslink[0].text
                    pattern=re.compile('\d\d\d\d')
                    cityeararr=re.findall(pattern,details)
                    if(len(cityeararr)>0):
                        cityear=cityeararr[-1] 
              
                addinf=details.split('-') 
                authorslist=""
                if(len(addinf)>0):
                    authorslist = addinf[0] 
                citauthors=authorslist.split(',') 
                for i in range(0,len(citauthors)):
                    if(isinstance(citauthors[i],str)):
                        citauthors[i]=''.join(i for i in citauthors[i] if ord(i)<128)
                paper=''.join(i for i in str(paper) if ord(i)<128)
                add_name= ''.join(i for i in str(add_name) if ord(i)<128)
                print(authors)
                print(citauthors)
                res=compareaut(authors,citauthors)
                print(res)
                print(cityear)
                if(year=="" or cityear==""):
                        if(res>=0.9):
                             tit_res=comparetit(paper,add_name)
                             print(paper)
                             print(add_name)
                             print(tit_res)
                             if(tit_res>= 0.3):
                                   eachone_dict={}
                                   eachone_list=[]
                                   if(unit_link !=""):
                                        eachone_dict[unit_name]=unit_link
                                        eachone_list.append(unit_name)
                                        eachone_list.append(details)
                                        eachone_dict[pdftext]=pdflink
                                        eachone_list.append(pdftext)
                                        surrogates_list.append(eachone_list)
                                        surrogates_dict[unit_name]=eachone_dict
                        elif(res>=0.5):
                             tit_res=comparetit(paper,add_name)
                             print(paper)
                             print(add_name)
                             print(tit_res)
                             if(tit_res>= 0.5):
                                   eachone_dict={}
                                   eachone_list=[]
                                   if(unit_link !=""):
                                        eachone_dict[unit_name]=unit_link
                                        eachone_list.append(unit_name)
                                        eachone_list.append(details)
                                        eachone_dict[pdftext]=pdflink
                                        eachone_list.append(pdftext)
                                        surrogates_list.append(eachone_list)
                                        surrogates_dict[unit_name]=eachone_dict
				        
                        elif(res>=0.1):
                             tit_res=comparetit(paper,add_name)
                             print(paper)
                             print(add_name)
                             print(tit_res)
                             if(tit_res>= 0.7):
                                   eachone_dict={}
                                   eachone_list=[]
                                   if(unit_link !=""):
                                        eachone_dict[unit_name]=unit_link
                                        eachone_list.append(unit_name)
                                        eachone_list.append(details)
                                        eachone_dict[pdftext]=pdflink
                                        eachone_list.append(pdftext)
                                        surrogates_list.append(eachone_list)
                                        surrogates_dict[unit_name]=eachone_dict
				 



                elif(compareyear(year,cityear)==1):
                        if(res>=0.9):
                             tit_res=comparetit(paper,add_name)
                             print(paper)
                             print(add_name)
                             print(tit_res)
                             if(tit_res>=0.3):
                                   eachone_dict={}
                                   eachone_list=[]
                                   if(unit_link !=""):
                                        eachone_dict[unit_name]=unit_link
                                        eachone_list.append(unit_name)
                                        eachone_list.append(details)
                                        eachone_dict[pdftext]=pdflink
                                        eachone_list.append(pdftext)
                                        surrogates_list.append(eachone_list)
                                        surrogates_dict[unit_name]=eachone_dict
                        elif(res>=0.5):
                             tit_res=comparetit(paper,add_name)
                             print(paper)
                             print(add_name)
                             print(tit_res)
                             if(tit_res>= 0.5):
                                   eachone_dict={}
                                   eachone_list=[]
                                   if(unit_link !=""):
                                        eachone_dict[unit_name]=unit_link
                                        eachone_list.append(unit_name)
                                        eachone_list.append(details)
                                        eachone_dict[pdftext]=pdflink
                                        eachone_list.append(pdftext)
                                        surrogates_list.append(eachone_list)
                                        surrogates_dict[unit_name]=eachone_dict
				        
                        elif(res>=0.1):
                             tit_res=comparetit(paper,add_name)
                             print(paper)
                             print(add_name)
                             print(tit_res)
                             if(tit_res>= 0.7):
                                   eachone_dict={}
                                   eachone_list=[]
                                   if(unit_link !=""):
                                        eachone_dict[unit_name]=unit_link
                                        eachone_list.append(unit_name)
                                        eachone_list.append(details)
                                        eachone_dict[pdftext]=pdflink
                                        eachone_list.append(pdftext)
                                        surrogates_list.append(eachone_list)
                                        surrogates_dict[unit_name]=eachone_dict
               
                                     
                         
    return (surrogates_list,surrogates_dict)       
 
def comparetit(paper,cit_unit_name):
    paperlist=re.split('[  -/]',paper)
    cit_unit_namelist=re.split('[  -/]',cit_unit_name)
    
    for i in range(0,len(paperlist)):
        paperlist[i]=paperlist[i].strip().replace(":","")
        paperlist[i]=paperlist[i].lower().replace(":","")
        #print(type( paperlist[i]))
    for i in range(0,len(cit_unit_namelist)):
        cit_unit_namelist[i]=cit_unit_namelist[i].strip().replace(":","")
        cit_unit_namelist[i]=cit_unit_namelist[i].lower().replace(":","")
        #print(type(cit_unit_namelist[i]))
    if(isinstance(paperlist[0],str)):
        paperlist=[x.encode('utf8') for x in paperlist]
    # print paperlist
    paperlist=remove_stopwords(paperlist)
    paperlist=stem(paperlist)
    if(isinstance(cit_unit_namelist[0],str)):
        cit_unit_namelist=[x.encode('utf8') for x in cit_unit_namelist]
    cit_unit_namelist=remove_stopwords(cit_unit_namelist)  
    cit_unit_namelist=stem(cit_unit_namelist)  
    v1, v2 = build_vector(paperlist, cit_unit_namelist)
    print(paperlist)
    print(cit_unit_namelist)
    return calculate_cosim(v1, v2)

def compareyear(year,cityear):
    if(isinstance(year,str)):
        year=year.encode('utf8') 
    if(isinstance(cityear,str)):
        cityear=cityear.encode('utf8')
    print(year)
    print(cityear)
    print((int(year)-int(cityear)))
    if(((int(year)-int(cityear))<=3 and (int(year)-int(cityear))>=0) or (int(cityear)-int(year))<=3 and (int(cityear)-int(year))>=0):
        return 1
    else:
        return 0
    

def remove_stopwords(word_list):
    for i in range(0,len(word_list)):
        if(isinstance(word_list[i],bytes)):
              word_list[i]=word_list[i].decode() 
    print(word_list)  
    resultwords  =[word for word in word_list if word not in stopwords.words('english')]
    print(resultwords)
    return resultwords

def stem(wordlist):
    resultwords=[]
    for i in range(0,len(wordlist)):
         wordlist[i]=wordlist[i].replace("?","")
    for i in range(0,len(wordlist)):
         resultwords.append(PorterStemmer().stem(wordlist[i]))
    
    return resultwords

def compareaut(authors,citauthors):
    for i in range(0,len(authors)):
        authors[i]=authors[i].strip()
        authors[i]=authors[i].lower()
        
    for i in range(0,len(citauthors)):
        citauthors[i]=citauthors[i].strip()
        citauthors[i]=citauthors[i].lower()
    
    print(jaccard(authors,citauthors))  
    return jaccard(authors,citauthors)
     
    
                     
def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2
 
def calculate_cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return round(dot_product / (magnitude1 * magnitude2),1) 

def jaccard(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    if(union_cardinality!=0):
        return round(intersection_cardinality/float(union_cardinality),1)
    else:
        return 0  


if __name__ == '__main__':
    reload(sys)
    #sys.setdefaultencoding('utf8')
    main()

