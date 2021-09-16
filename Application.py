from os import close
from tkinter import *
from tkinter import filedialog

ws = Tk()
ws.title("ABEEWAY APP LOG ANALYSER")
ws.geometry("1200x1200")
ws['bg']='#33C1FF'
pathh = Entry(ws)
pathh.pack(side="bottom",expand=True, fill=X, padx=20)


def add_tracker():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    addtracker_keywords = ['FlowType.ADD_TRACKER 1.yes','FlowType.ADD_TRACKER 2.yes','FlowType.ADD_TRACKER 2.no.2','FlowType.ADD_TRACKER 3.yes.yes.no','FlowType.ADD_TRACKER 3.yes.yes.yes','FlowType.ADD_TRACKER 3.no.yes.yes','FlowType.ADD_TRACKER 3.no.no', 'FlowType.ADD_TRACKER 4.no','FlowType.ADD_TRACKER 4.yes.yes','FlowType.ADD_TRACKER 5.no','FlowType.ADD_TRACKER 5.yes.yes','FlowType.ADD_TRACKER 7.no','FlowType.ADD_TRACKER 7.yes.yes','FlowType.ADD_TRACKER end']
    f= open("result.txt","w+")
    f.truncate(0)
    for line in tf :
      for k in addtracker_keywords:
       if k in line:
         print(k)
         if k == 'FlowType.ADD_TRACKER 1.yes':
              print("SUCCESS- Tracker found from Blutooth Adverstisement list!")
              f.write("SUCCESS !- Tracker found from Blutooth Adverstisement list - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 2.no.2':
              print("SUCCESS- Read tracker HW ID +ABW XXX (Tracker Name) without onding and ABW XXX converted to DEVUI")
              f.write("SUCCESS- Read tracker HW ID +ABW XXX (Tracker Name) without Bonding and ABW XXX converted to DEVUI - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 3.no.no':
              print("SUCCESS- Connect and bond with tracker,communication with tracker via BLE")
              f.write("SUCCESS- Connect and bond with tracker,communication with tracker via BLE - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 3.no.yes.yes':
              print("FAILURE- connect and  ble bond with tracker 3rd time attempt failed")
              f.write("FAILURE- connect and  ble bond with tracker 3rd time attempt failed - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 4.no':
              print("SUCCESS- Tracker parameter is set default!")
              f.write("SUCCESS- Tracker parameter is set default! - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 4.yes.yes':
              print("FAILURE- Tracker default Parameter initilization 3rd attempt failed")
              f.write("FAILURE- Tracker default Parameter initilization 3rd attempt failed - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 5.yes.yes':
              print("FAILURE- Tracker feed call API tracker parameter to backend 3rd attempt failed")
              f.write("FAILURE- Tracker feed call API tracker parameter to backend 3rd attempt failed - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 7.no':
              print("SUCCESS- API call to add name/image in TPX Media")  
              f.write("SUCCESS- API call to add name/image in TPX Media - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER end':
              print("SUCCESS- Add-Tracker process completed!")    
              f.write("SUCCESS- Add-Tracker process completed! - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 2.yes':
              print("FAILURE- BLE connection to the tracker has failed") 
              f.write("FAILURE- BLE connection to the tracker has failed - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 3.yes.yes.no':
              print("FAILURE- API call to register the tracker failed") 
              f.write("FAILURE- API call to register the tracker failed - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 3.yes.yes.yes':
              print("FAILURE- Tracker registered in another account") 
              f.write("FAILURE- Tracker registered in another account - %s\r\n" %k)

         if k == 'FlowType.ADD_TRACKER 7.yes.yes':
              print("FAILURE- Tracker Customisation API call Failed") 
              f.write("FAILURE- Tracker Customisation API call Failed - %s\r\n" %k)
def firmware_update():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    keywords = ['BLE:  connectDevice, isConnected: true Device','Connection to the tracker failed with Error Code','Failed to read MCU Firmware Version of the tracker','API Call to retrieve MCU Failed with Error Code','MCU Firmware Version retrieval from tracker failed with','Failed to read BLE Firmware Version of the tracker','HTTP:  Successfully Received Latest BLE Firmware Version: {firmwareFile: FirmwareFileBLE','HTTP:  Successfully Received Latest MCU Firmware Version: {firmwareFile: FirmwareFileMCU','FlowType.FIRMWARE_UPDATE Setup Update Of FirmwareUpdateType.ble',' FlowType.FIRMWARE_UPDATE BLE DFU Update started','FlowType.FIRMWARE_UPDATE BLE DFU Update ended','BLE Firmware Update failed with','BLE Firmware Version retrieval from tracker failed with','MCU Firmware Update failed','FlowType.FIRMWARE_UPDATE Setup Update Of FirmwareUpdateType.mcu','HTTP:  Successfully Downloaded Latest MCU Firmware','FlowType.FIRMWARE_UPDATE Enable MCU Firmware Update','FlowType.FIRMWARE_UPDATE New Version FirmwareUpdateType.mcu','Failed to re-establish connection with the tracker after Firmware update','API Call to retrieve BLE Failed with Error Code','API Call to retrieve BLE Failed with Error Code','FlowType.FIRMWARE_UPDATE New Version FirmwareUpdateType.ble']
    f= open("Result.txt","w+")

    for line in tf :
      for k in keywords:
    
       if k in line:
         print(k)
         if k == 'BLE:  connectDevice, isConnected: true Device':
              print("SUCCESS- Tracker connected and bonded")
              f.write("SUCCESS- Tracker connected and bonded \r\n" )

         if k == 'Connection to the tracker failed with Error Code':
              print("FAILURE - Intial Bluetthooth Connectivity error")
              f.write("FAILURE - Intial Bluetthooth Connectivity error \r\n" )

         if k == 'Failed to read MCU Firmware Version of the tracker':
              print("FAILURE - Current MCU Version is not read via BLE connection")
              f.write("FAILURE - Current MCU Version is not read via BLE connection \r\n" )

         if k == 'Failed to read BLE Firmware Version of the tracker':
              print("FAILURE - Current BLE Version is not read via BLE connection")
              f.write("FAILURE - Current BLE Version is not read via BLE connection\r\n" )
         

         if k == 'API Call to retrieve MCU Failed with Error Code':
              print("FAILURE - API call to fetch MCU FW File Failed")
              f.write("FAILURE - API call to fetch MCU FW File Failed\r\n" )

         if k == 'MCU Firmware Version retrieval from tracker failed with ':
              print("FAILURE - MCU Firmware Version retrieval from tracker failed")
              f.write("FAILURE - MCU Firmware Version retrieval from tracker failed (FlowType.FIRMWARE_UPDATE 13.no.no.yes.no)\r\n" )

         if k == 'BLE Firmware Update failed with ':
              print("FAILURE - BLE Firmware Update failed ")
              f.write("FAILURE - BLE Firmware Update failed  (FlowType.FIRMWARE_UPDATE 11.yes)\r\n" )

         if k == 'BLE bond removal for the tracker has failed with error Code':
              print("FAILURE - After Updation App has Failed to remove the bond")
              f.write("FAILURE - After Updation App has Failed to remove the bond (FlowType.FIRMWARE_UPDATE 15.yes.no)\r\n" )

         if k == 'BLE Firmware Version retrieval from tracker failed with ':
              print("FAILURE - BLE Firmware Version retrieval from tracker failed")
              f.write("FAILURE - BLE Firmware Version retrieval from tracker failed (FlowType.FIRMWARE_UPDATE 12 yes.yes.no)\r\n" )
          
         if k == 'MCU Firmware Update failed':
              print("FAILURE - MCU Firmware Update failed")
              f.write("FAILURE - MCU Firmware Update failed (FlowType.FIRMWARE_UPDATE 13.no.yes)\r\n" )

         
         if k == 'Failed to re-establish connection with the tracker after Firmware update':
              print("FAILURE -re-establish connection with the tracker after Firmware update")
              f.write("FAILURE -re-establish connection with the tracker after Firmware update (FlowType.FIRMWARE_UPDATE 13.yes.yes )\r\n" )

         if k == 'HTTP:  Successfully Received Latest BLE Firmware Version: {firmwareFile: FirmwareFileBLE':
              print("Successfully Received Latest BLE Firmware Version")
              f.write("SUCCESS- Received Latest BLE Firmware Version \r\n" )

         if k == 'HTTP:  Successfully Received Latest MCU Firmware Version: {firmwareFile: FirmwareFileMCU':
              print("Successfully Received Latest MCU Firmware Version")
              f.write("SUCCESS- Successfully Received Latest MCU Firmware Version! \r\n" )

         if k == 'FlowType.FIRMWARE_UPDATE Setup Update Of FirmwareUpdateType.ble':
              print("SUCCESS- API call for BLE  Firmware ")
              f.write("SUCCESS- API call for BLE  Firmware\r\n" )

         if k == ' FlowType.FIRMWARE_UPDATE BLE DFU Update started':
              print("SUCCESS - Fast connection is enabled and BLE parameter exchange happen")
              f.write("SUCCESS - Fast connection is enabled and BLE parameter exchange happen \r\n" )

         if k == 'FlowType.FIRMWARE_UPDATE BLE DFU Update ended':
              print("SUCCESS- BLE firmware update is succesfull")  
              f.write("SUCCESS- BLE firmware update is succesfull  \r\n" )

         if k == 'FlowType.FIRMWARE_UPDATE Setup Update Of FirmwareUpdateType.mcu':
              print("SUCCESS- MCU Firmware update initialsed!")    
              f.write("SUCCESS- MCU Firmware update initialsed!! \r\n" )

         if k == 'HTTP:  Successfully Downloaded Latest MCU Firmware':
              print("SUCCESS - Latest MCU Firware Downloaded from Backend") 
              f.write("SUCCESS - Latest MCU Firware Downloaded from Backend \r\n" )

         if k == 'FlowType.FIRMWARE_UPDATE Enable MCU Firmware Update':
              print("SUCCESS -MCU Firmware BLE Parameter exchange started") 
              f.write("SUCCESS -MCU Firmware BLE Parameter exchange started \r\n" )

         if k == 'FlowType.FIRMWARE_UPDATE New Version FirmwareUpdateType.mcu':
              print("SUCCESS- MCU Tracker Firmware update is Successfull") 
              f.write("SUCCESS- MCU Tracker Firmware update is Successfull \r\n" )

         #if k == 'FlowType.FIRMWARE_UPDATE New Version FirmwareUpdateType.ble':
             # print("SUCCESS- BLE MCU Firemware Updated") 
             # f.write("SUCCESS- BLE MCU Firemware Updated - %s\r\n" %k)
def motion_BLE():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    motion_keywords = ['Successfully Created Tracker Alert: {alertType: {alertTypeName: AlertTypeMotion','BLE:  system: 1','eventType: MOTION_START','title_loc_key: NOTIFICATION_TITLE_MOTION','onFirebaseMessage: {click_action: FLUTTER_NOTIFICATION_CLICK','BLE:  system: 2','eventType: MOTION_END','notifyOnInterface: false']
    f= open("result.txt","w+")
    f.write("BLE CONNECTED MOTION ANALYSIS (STEP1 + STEP 2 + STEP 3 + STEP 4 + STEP 5 + STEP 6 + STEP 7) \r\n")
    f.write("---------------------------------------------------------------------------\r\n")
    for line in tf :
      for k in motion_keywords:
       if k in line:
         print(k)
         if k == 'Successfully Created Tracker Alert: {alertType: {alertTypeName: AlertTypeMotion':
              print("SUCCESS- Motion Alert created by User")
              f.write("STEP 1-SUCCESS- Motion Alert created by User \r\n")

         if k == 'BLE:  system: 1':
              print("SUCCESS- Tracker sends Motion start via BLE")
              f.write("STEP 2 -SUCCESS- Tracker sends Motion start via BLE\r\n")

         if k == 'eventType: MOTION_START':
              print("SUCCESS - The Motion event is send to backend")
              f.write("STEP 3 -SUCCESS- The Motion event is send to backend \r\n")

         if k == 'title_loc_key: NOTIFICATION_TITLE_MOTION' and 'onFirebaseMessage: {click_action: FLUTTER_NOTIFICATION_CLICK':
              print("SUCCESS- Motion notification recieved from Backend")
              f.write("STEP 4 -SUCCESS- Motion notification recieved from Backend\r\n" )

         if k == 'BLE:  system: 2':
              print("SUCCESS- Motion stop recevied  from trcaker via BLE")
              f.write("STEP 5 -SUCCESS- Motion stop recevied  from trcaker via BLE\r\n")

         if k == 'eventType: MOTION_END':
              print("SUCCESS - The motion end event is send to backend")
              f.write("STEP 6 -SUCCESS - The motion end event is send to backend\r\n")

         if k == 'notifyOnInterface: false':
              print("SUCCESS- user disabled the motion alert")
              f.write("STEP 7 -SUCCESS- user disabled the motion alert\r\n")
def motion_LORA():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    motion_LORA_keywords = ['AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeMotion"','notifyOnInterface: true}','title_loc_key: NOTIFICATION_TITLE_MOTION','onFirebaseMessage: {click_action: FLUTTER_NOTIFICATION_CLICK','notifyOnInterface: false']
    f= open("result.txt","w+")
    f.write("LORA CONNECTED MOTION ANALYSIS (STEP1 - Motion_Alert created by User + STEP 2 - Notification recieved + STEP 3 - User disabled the Motion_Alert) \r\n")
    f.write("------------------------------------------------------------------------------------------------------------------------------------------------\r\n")
    for line in tf :
      for k in motion_LORA_keywords :
       if k in line:
         print(k)
         if k == 'Successfully Created Tracker Alert: {alertType: {alertTypeName: AlertTypeMotion' and 'notifyOnInterface: true}':
              print("SUCCESS- Motion Alert created by User")
              f.write("STEP 1-SUCCESS- Motion Alert created by User \r\n")

         if k == 'title_loc_key: NOTIFICATION_TITLE_MOTION' and 'onFirebaseMessage: {click_action: FLUTTER_NOTIFICATION_CLICK':
              print("SUCCESS- Motion notification recieved from Backend")
              f.write("STEP 2 -SUCCESS- Motion notification recieved from Backend\r\n" )


         if k == 'Successfully Created Tracker Alert: {alertType: {alertTypeName: AlertTypeMotion' and 'notifyOnInterface: false':
              print("SUCCESS- user disabled the motion alert")
              f.write("STEP 3 -SUCCESS- Alerts_API Called for user disabled the motion alert\r\n")
def SOS_BLE():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    SOS_BLE_keywords = ['{"alertTypeName":"AlertTypeSoS"','"notifyOnInterface":true','BLE:  system: 0','onFirebaseMessage:','body_loc_key: NOTIFICATION_BODY_SOS','title_loc_key: NOTIFICATION_TITLE_SOS','BLE:  system: 3','sosFlag: false']
    f= open("result.txt","w+")
    f.write("BLE CONNECTED SOS ANALYSIS\r\n")
    f.write("(STEP1 - SOS Alert created by User + STEP 2 - Tracker send SOS Alert to APP + STEP 3 - The SOS Alert is notificied to backend via feed Api + STEP 4 - Tracker send SOS STOP Alert to APP + STEP 5 - SOS Stop alert from Backend feed API+ STEP 6 - SOS Alert disabled by User in APP) \r\n")

    f.write("---------------------------------------------------------------------------------------------------------------------------------\r\n")
    for line in tf :
      for k in SOS_BLE_keywords :
       if k in line:
         print(k)
         if k == '{"alertTypeName":"AlertTypeSoS"' and '"notifyOnInterface":true':
              print("SUCCESS- SOS Alert created by User")
              f.write("STEP 1-SUCCESS- SOS Alert created by User \r\n")

         if k == 'BLE:  system: 0':
              print("SUCCESS- Tracker send SOS Alert to APP")
              f.write("STEP 2 -SUCCESS- Tracker send SOS Alert to APP\r\n" )


         if k == 'sosFlag: true' :
              print("SUCCESS- The SOS Alert is notificied to backend via feed Api")
              f.write("STEP 3 -SUCCESS- The SOS Alert is notificied to backend via feed Api\r\n")

         if k == 'onFirebaseMessage:' and 'title_loc_key: NOTIFICATION_TITLE_SOS' and 'body_loc_key: NOTIFICATION_BODY_SOS' :
              print("SUCCESS- The mobile APP receives push notification indicating SoS alert")
              f.write("STEP 3 -SUCCESS- The mobile APP receives push notification indicating SoS alert\r\n")

         if k == 'BLE:  system: 3' :
              print("SUCCESS- Tracker send SOS STOP Alert to APP")
              f.write("STEP 4 -SUCCESS- Tracker send SOS STOP Alert to APP\r\n" )

         if k == 'sosFlag: false':
              print("SUCCESS- SOS Stop alert from Backend feed API")
              f.write("STEP 5 -SUCCESS- SOS Stop alert from Backend feed API\r\n" )

         if k == '{"alertTypeName":"AlertTypeSoS"' and '"notifyOnInterface":false':
              print("SUCCESS- SOS Alert disabled by User in APP")
              f.write("STEP 6-SUCCESS- SOS Alert disabled by User in APP \r\n")
def SOS_LORA():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    SOS_LORA_keywords = ['{"alertTypeName":"AlertTypeSoS"','"notifyOnInterface":true','BLE:  system: 0','onFirebaseMessage:','body_loc_key: NOTIFICATION_BODY_SOS','title_loc_key: NOTIFICATION_TITLE_SOS','BLE:  system: 3','sosFlag: false']
    f= open("result.txt","w+")
    f.write("LORAWAN CONNECTED SOS ANALYSIS\r\n")
    f.write(" STEP 1 - SOS Alert created by User + STEP 2 - SOS notification recieved from Backend+ STEP 3 -  Alerts_API Called for user disabled the SOS alert \r\n")

    f.write("---------------------------------------------------------------------------------------\r\n")
    for line in tf :
      for k in SOS_LORA_keywords :
       if k in line:
         print(k)
         if k == '{"alertTypeName":"AlertTypeSOS"' and '"notifyOnInterface":true':
              print("SUCCESS- SOS Alert created by User")
              f.write("STEP 1-SUCCESS- SOS Alert created by User in APP\r\n")
        
         if k == 'title_loc_key: NOTIFICATION_TITLE_SOS' and 'onFirebaseMessage: {click_action: FLUTTER_NOTIFICATION_CLICK':
              print("SUCCESS- SOS notification recieved from Backend")
              f.write("STEP 2 -SUCCESS- SOS notification recieved from Backend\r\n" )


         if k == 'Successfully Created Tracker Alert: {alertType: {alertTypeName: AlertTypeSOS' and 'notifyOnInterface: false':
              print("SUCCESS- user disabled the SOS alert")
              f.write("STEP 3 -SUCCESS- Alerts_API Called for user disabled the SOS alert\r\n")
def Sharing_LORA():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    Sharing_LORA_keywords = ['Successfully Shared Tracker','onFirebaseMessage: {click_action:FLUTTER_NOTIFICATION_CLICK','body_loc_key: NOTIFICATION_BODY_SHARE_START','type: SHARE_START','{"alertType":{"alertTypeName":"AlertTypeSoS"','"notifyOnInterface":true}','{"alertType":{"alertTypeName":"AlertTypeMotion"','NOTIFICATION_BODY_MOTION','NOTIFICATION_TITLE_MOTION','NOTIFICATION_BODY_SOS','NOTIFICATION_TITLE_SOS','notifyOnInterface":false}']
    f= open("result.txt","w+")
    f.write("LORAWAN CONNECTED SHARING ANALYSIS\r\n")
    f.write(" STEP 1a - Tracker is shared with another user\r\n")
    f.write(" STEP 1b - Push notification that arrives on follower’s phone\r\n")
    f.write(" STEP 2A - user enabled the SOS alert in secondary APP UI\r\n")
    f.write(" STEP 2B - user enabled the MOTION alert in secondary APP UI\r\n")
    f.write(" STEP 3A - Motion Alert Notification recieved in secondary phone\r\n")
    f.write(" STEP 3B - SoS Alert Notificaton recieved in secondary phone\r\n")
    f.write(" STEP 4A -SUCCESS- Alerts_API Called for user Disabled the SOS alert in APP UI \r\n")
    f.write(" STEP 4B -SUCCESS- Alerts_API Called for user Disabled the Motion alert in APP UI  \r\n") 
    f.write("---------------------------------------------------------------------------------------\r\n")
    for line in tf :
      for k in Sharing_LORA_keywords:
       if k in line:
         print(k)
         if k == 'Successfully Shared Tracker':
              print("SUCCESS - The Tracker is shared with another user")
              f.write("STEP 1A-SUCCESS- The primary tracker is shared with another user in primary phone\r\n")
        
         if k == 'onFirebaseMessage: {click_action:FLUTTER_NOTIFICATION_CLICK' and 'body_loc_key: NOTIFICATION_BODY_SHARE_START' and 'type: SHARE_START':
              print("SUCCESS- Push notification that arrives on follower’s phone and also email indicating the sharing of the tracker")
              f.write("STEP 1B -SUCCESS- Push notification that arrives on follower’s phone and also email indicating the sharing of the tracker\r\n" )


         if k == '{"alertType":{"alertTypeName":"AlertTypeSoS"' and '"notifyOnInterface":true}':
              print("SUCCESS- User enabled the SOS alert")
              f.write("STEP 2A -SUCCESS- Alerts_API Called for user enabled the SOS alert in  secondary APP UI\r\n")

         if k == '{"alertType":{"alertTypeName":"AlertTypeMotion"' and '"notifyOnInterface":true}':
              print("SUCCESS- User enabled the MOTION alert")
              f.write("STEP 2B -SUCCESS- Alerts_API Called for user enabled the MOTION alert in  secondary APP UI\r\n")

         if k == 'onFirebaseMessage: {click_action:FLUTTER_NOTIFICATION_CLICK' and 'NOTIFICATION_BODY_MOTION,' and 'NOTIFICATION_TITLE_MOTION':
              print("SUCCESS- Mobile APP receives  Motion alert push notification from the backend")
              f.write("STEP 3A -SUCCESS- Mobile APP receives Motion alert push notification from the backend\r\n")

         if k == 'onFirebaseMessage: {click_action:FLUTTER_NOTIFICATION_CLICK' and 'NOTIFICATION_BODY_SOS,' and 'NOTIFICATION_TITLE_SOS':
              print("SUCCESS- Mobile APP receives  SOS alert push notification from the backend")
              f.write("STEP 3B -SUCCESS- Mobile APP receives SOS alert push notification from the backend\r\n")

         if k == '{"alertType":{"alertTypeName":"AlertTypeSoS"' and '"notifyOnInterface":false}':
              print("SUCCESS- User Disabled  the SOS alert")
              f.write("STEP 4A -SUCCESS- Alerts_API Called for user Disabled the SOS alert in APP UI\r\n")

         if k == '{"alertType":{"alertTypeName":"AlertTypeMotion"' and '"notifyOnInterface":false}':
              print("SUCCESS- User Disabled the Motion alert")
              f.write("STEP 4B -SUCCESS- Alerts_API Called for user Disabled the Motion alert in APP UI\r\n")
def pod():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    pod_keyword = ['AbeewayHttpClient Body:{"trackerCommandType":"TrackerCommandToSendRequest"','API call to request tracker position failed','WEBSOCKET: Got JSON Websocket Data: {"kind":"UplinkReceived"','Tracker position request failed','Tracker position change was successful”']
    f= open("result.txt","w+")
    

    for line in tf :
      for k in pod_keyword :
       if k in line:
         print(k)

         if k == 'AbeewayHttpClient Body:{"trackerCommandType":"TrackerCommandToSendRequest"':
              print("SUCCESS- API Call request the position of the with downlink tracker command ")
              f.write("STEP 1 - API Call request the position of the with downlink tracker command\r\n")
         if k == 'API call to request tracker position failed':
              print("FAILURE- API call to request tracker position failed ")
              f.write("FAILURE - API call to request tracker position failed after 3 tries\r\n")
         if k == 'WEBSOCKET: Got JSON Websocket Data: {"kind":"UplinkReceived"':
              print("SUCCESS - Wait for push notification from the backend or position update from websocket")
              f.write("SUCCESS - Wait for push notification from the backend or position update from websocket\r\n")
         if k == 'Tracker position request failed':
              print("FAILURE - 20 Mints timer exceeded .No POD Received")
              f.write("FAILURE - 20 Mints timer exceeded .No POD Received\r\n")
         if k == 'Tracker position change was successful':
              print("SUCCESS -  Position on demand recieved")
              f.write("SUCCESS -  Position on demand recieved\r\n")         
def Sharing_BLE():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    Sharing_BLE_keywords = ['Successfully Shared Tracker','BLE:  system: 1','eventType:MOTION_START','BLE:  system: 0','sosFlag: true','BLE: system: 3','sosFlag: false','title_loc_key:NOTIFICATION_TITLE_SHARE_START','AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeMotion","notifyByEmail":false,"notifyOnInterface":true','AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeSOS","notifyByEmail":false,"notifyOnInterface":true','AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeMotion","notifyByEmail":false,"notifyOnInterface":false','AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeSOS","notifyByEmail":false,"notifyOnInterface":false','title_loc_key: NOTIFICATION_TITLE_SOS','body_loc_key:NOTIFICATION_BODY_SOS','title_loc_key: NOTIFICATION_TITLE_MOTION','body_loc_key:NOTIFICATION_BODY_MOTION']
    f= open("result.txt","w+")
    f.write("BLE CONNECTED SHARING FEATURE ANALYSIS\r\n")
    f.write(" STEP 1A (Primary Phone)- The user shares the tracker from the primary account to the follower account\r\n")
    f.write(" STEP 1B (Primary Phone)- Motion Start event received from Tracker\r\n")
    f.write(" STEP 1B.1 (Primary Phone)- Motion Start event sent to backend API\r\n")
    f.write(" STEP 1C (Primary Phone)- Motion STOP event received from Tracker\r\n")
    f.write(" STEP 1C.1 (Primary Phone)- Motion Stop event sent to backend API\r\n")
    f.write(" STEP 1D (Primary Phone)- SOS Start event received from Tracker\r\n")
    f.write(" STEP 1D.1 (Primary Phone)- SOS Start event sent to backend API\r\n")
    f.write(" STEP 1E (Primary Phone)- SOS STOP event received from Tracker\r\n")
    f.write(" STEP 1E.1 (Primary Phone)- SOS Stop event sent to backend API  \r\n") 
    f.write("--------------------------------------------------------------------------------------------------------\r\n")
    f.write(" STEP 2A (Secondary Phone) -Push notification that arrives on follower’s phone and also email indicating the tracker that has just been shared\r\n")
    f.write(" STEP 2B.1 (Secondary Phone) -user enabled Motion Alert in App UI\r\n")
    f.write(" STEP 2B.2 (Secondary Phone) -user enabled SOS Alert in App UI\r\n")
    f.write(" STEP 2C.1 (Secondary Phone) -Motion Notification recieved in Secondary Phone\r\n")
    f.write(" STEP 2C.2 (Secondary Phone) -SOS Notification recieved in Secondary Phone\r\n")
    f.write(" STEP 3D.1 (Secondary Phone) -Alerts_API Called for user Disabled the SOS alert in APP UI\r\n")
    f.write(" STEP 3D.2  (Secondary Phone) -Alerts_API Called for user Disabled the Motion alert in APP UI\r\n")
    f.write("--------------------------------------------------------------------------------------------------------\r\n")

    for line in tf :
      for k in Sharing_BLE_keywords :
       if k in line:
         print(k)
         if k == 'Successfully Shared Tracker':
              print("SUCCESS- The user shares the tracker from the primary account to the follower account")
              f.write("STEP 1A-The user shares the tracker from the primary account to the follower account\r\n")

         if k == 'BLE:  system: 1':
              print("SUCCESS- Motion Start event received from Tracker")
              f.write("STEP 1B -SUCCESS- Motion Start event received from Tracker\r\n" )

         if k == 'eventType:MOTION_START':
              print("SUCCESS- Motion Start event sent to backend API")
              f.write("STEP 1B.1 -SUCCESS- Motion Start event sent to backend API %s\r\n" %k)

         if k == 'BLE: system: 2' :
              print("SUCCESS- Motion STOP event received from Tracker")
              f.write("STEP 1C -SUCCESS- Motion STOP event received from Tracker\r\n")

         if k == 'eventType:MOTION_END,':
              print("SUCCESS- Motion Stop event sent to backend API")
              f.write("STEP 1C.1 -SUCCESS- Motion Stop event sent to backend API\r\n" )

         if k == 'BLE:  system: 0':
              print("SUCCESS- SOS Start event received from Tracker")
              f.write("STEP 1D -SUCCESS- SOS Start event received from Tracker\r\n" )
         
         if k == 'sosFlag: true':
              print("SUCCESS- SOS Start event sent to backend API")
              f.write("STEP 1D.1 -SUCCESS- SOS Start event sent to backend API\r\n" )
              
         if k == 'BLE: system: 3' :
              print("SUCCESS- SOS STOP event received from Tracker")
              f.write("STEP 1E -SUCCESS- SOS STOP event received from Tracker\r\n")

         if k == 'sosFlag: false':
              print("SUCCESS- SOS Stop event sent to backend API")
              f.write("STEP 1E.1 -SUCCESS- SOS Stop event sent to backend API\r\n" )   
         
         if k == 'title_loc_key:NOTIFICATION_TITLE_SHARE_START':
              print("SUCCESS- push notification that arrives on follower’s phone and also email indicating the tracker that has just been shared")
              f.write("STEP 2A -SUCCESS- push notification that arrives on follower’s phone and also email indicating the tracker that has just been shared\r\n" )   

         if k == 'AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeMotion","notifyByEmail":false,"notifyOnInterface":true':
              print("SUCCESS- user enabled Motion Alert in App UI")
              f.write("STEP 2B.1 -SUCCESS- APi  call user enabled Motion Alert in App UI\r\n" )   
 
         if k == 'AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeSOS","notifyByEmail":false,"notifyOnInterface":true':
              print("SUCCESS- user enabled SOS Alert in App UI")
              f.write("STEP 2B.2 -SUCCESS- user enabled SOS Alert in App UI\r\n" )  
         
         if k == 'body_loc_key:NOTIFICATION_BODY_MOTION' and 'title_loc_key: NOTIFICATION_TITLE_MOTION':
              print("SUCCESS- Motion Notification recieved in Secondary Phone")
              f.write("STEP 2C.1 -SUCCESS- Motion Notification recieved in Secondary Phone\r\n" )  
          
         if k == 'body_loc_key:NOTIFICATION_BODY_SOS' and 'title_loc_key: NOTIFICATION_TITLE_SOS':
              print("SUCCESS- SOS Notification recieved in Secondary Phone")
              f.write("STEP 2C.2 -SUCCESS- SOS Notification recieved in Secondary Phone\r\n" )  

         if k == 'AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeSOS","notifyByEmail":false,"notifyOnInterface":false':
              print("SUCCESS- User Disabled  the SOS alert")
              f.write("STEP 2D.1 -SUCCESS- Alerts_API Called for user Disabled the SOS alert in APP UI\r\n")

         if k == 'AbeewayHttpClient Body: {"alertType":{"alertTypeName":"AlertTypeMotion","notifyByEmail":false,"notifyOnInterface":false':
              print("SUCCESS- User Disabled the Motion alert")
              f.write("STEP 2D.2 -SUCCESS- Alerts_API Called for user Disabled the Motion alert in APP UI\r\n")
def tracker_profile_change():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) 
    tracker_profile_change_keywords = ['SCREEN: FlowType.PROFILE 1','“Profile change will be applied after next periodic wake up of the tracker. It can take upto 20 no minutes','AbeewayHttpClient Body:{trackerCommandType:TrackerCommandToChangeProfile','profileName:','notifyOnInterface:true','Tracker profile change failed','due to the tracker out of range of LoRaWAN coverage. Please try again later','Tracker profile change was successful']
    f= open("result.txt","w+")
    

    for line in tf :
      for k in tracker_profile_change_keywords :
       if k in line:
         print(k)
         if k == 'SCREEN: FlowType.PROFILE 1':
              print("SUCCESS- The user requests to change the profile of the tracker")
              f.write("SUCCESS- The user requests to change the profile of the tracker\r\n")
          
         if k == '“Profile change will be applied after next periodic wake up of the tracker. It can take upto 20 no minutes':
              print("“Profile change will be applied after next periodic wake up of the tracker. It can take upto 20 no minutes")
              f.write("TRACKER LORAWAN CONNECTED - Profile change will be applied after next periodic wake up of the tracker. \r\n")

         if k == 'AbeewayHttpClient Body:{trackerCommandType:TrackerCommandToChangeProfile' and 'profileName:' and 'notifyOnInterface:true':
              print("Call the API to change the profile of the tracker using Downlink tracker command")
              f.write("TRACKER LORAWAN CONNECTED - Call the API to change the profile of the tracker using Downlink tracker command \r\n")

         if k == 'Tracker profile change failed':
              print("API Call to change profile of the tracker failed")
              f.write("TRACKER LORAWAN CONNECTED - API Call to change profile of the tracker failed after 3 trys \r\n")

         if k == 'due to the tracker out of range of LoRaWAN coverage. Please try again later':
              print("Push notification didn’t received after Waiting  for push notification from the backend 20mints")
              f.write("TRACKER LORAWAN CONNECTED - Push notification didn’t received after Waiting  for push notification from the backend 20mints \r\n")

         if k == 'Tracker profile change was successful':
              print("Tracker profile is Changed")
              f.write("TRACKER LORAWAN CONNECTED - Tracker profile change was successful \r\n")

def openFile1():
    txtarea = Text(ws, width=100, height=50)
    txtarea.pack(pady=5)
    f = open("result.txt", 'r')
    data = f.read()
    txtarea.insert(END, data)
    f.close()


Button(
    ws,
    text="ADD TRACKER ANALYSIS",command=add_tracker).pack(side=TOP, expand=True,padx=40)   
Button(
    ws,
    text="FIRMWARE UPDATE ANALYSIS",command=firmware_update).pack(side=TOP, expand=True, padx=40)
Button(
    ws,
    text="MOTION ANALYSIS : LORA",command=motion_LORA).pack(side=TOP, expand=True,padx=40)       
Button(
    ws,
    text=" MOTION ANALYSIS : BLE",command=motion_BLE).pack(side=TOP, expand=True, padx=40)
Button(
    ws,
    text=" SOS ANALYSIS : BLE",command=SOS_BLE).pack(side=TOP, expand=True, padx=40)
Button(
    ws,
    text=" SOS ANALYSIS : LORAWAN",command=SOS_LORA).pack(side=TOP, expand=True,  padx=40) 
Button(
    ws,
    text="SHARING-LORA : PRIMARY & SECONDARY",command=Sharing_LORA).pack(side=TOP, expand=True, padx=40)  
Button(
    ws,
    text="SHARING-BLE : PRIMARY & SECONDARY",command=Sharing_BLE).pack(side=TOP, expand=True, padx=40)
Button(
    ws,
    text="POD : Position on Demand ",command=pod).pack(side=TOP, expand=True, padx=40)   
Button(
    ws,
    text=" Show Results",command=openFile1).pack(side=BOTTOM,expand= False, fill=X, padx=40)
Button(
    ws,
    text="PROFILE CHANGE LORA  ",command=tracker_profile_change).pack(side=TOP, expand=True, padx=40) 


ws.mainloop()
