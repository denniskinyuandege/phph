 curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"InitiatorName\":\" \",
    \"SecurityCredential\":\" \",
    \"CommandID\":\" \",
    \"Amount\":\" \",
    \"PartyA\":\" \",
    \"PartyB\":\" \",
    \"Remarks\":\" \",
    \"QueueTimeOutURL\":\"http://your_timeout_url\",
    \"ResultURL\":\"http://your_result_url\",
    \"Occasion\":\" \"
  }" "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"InitiatorName\":\" \",
    \"SecurityCredential\":\" \",
    \"CommandID\":\" \",
    \"Amount\":\" \",
    \"PartyA\":\" \",
    \"PartyB\":\" \",
    \"Remarks\":\" \",
    \"QueueTimeOutURL\":\"http://your_timeout_url\",
    \"ResultURL\":\"http://your_result_url\",
    \"Occasion\":\" \"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "InitiatorName": " ",
    "SecurityCredential":" ",
    "CommandID": " ",
    "Amount": " ",
    "PartyA": " ",
    "PartyB": " ",
    "Remarks": " ",
    "QueueTimeOutURL": "http://your_timeout_url",
    "ResultURL": "http://your_result_url",
    "Occasion": " "
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
      json : {
        "InitiatorName": " ",
        "SecurityCredential":" ",
        "CommandID": " ",
        "Amount": " ",
        "PartyA": " ",
        "PartyB": " ",
        "Remarks": " ",
        "QueueTimeOutURL": "http://your_timeout_url",
        "ResultURL": "http://your_result_url",
        "Occasion": " "
      }
    },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'InitiatorName' => ' ',
    'SecurityCredential' => ' ',
    'CommandID' => ' ',
    'Amount' => ' ',
    'PartyA' => ' ',
    'PartyB' => ' ',
    'Remarks' => ' ',
    'QueueTimeOutURL' => 'http://your_timeout_url',
    'ResultURL' => 'http://your_result_url',
    'Occasion' => ' '
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :InitiatorName ""
        :SecurityCredential ""
        :CommandID ""
        :Amount ""
        :PartyA ""
        :PartyB ""
        :Remarks ""
        :QueueTimeOutURL "http://your_timeout_url"
        :ResultURL "http://your_result_url"
        :Occasion ""
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"InitiatorName\":\" \",
    \"SecurityCredential\":\" \",
    \"CommandID\":\" \",
    \"Amount\":\" \",
    \"PartyA\":\" \",
    \"PartyB\":\" \",
    \"Remarks\":\" \",
    \"QueueTimeOutURL\":\"http://your_timeout_url\",
    \"ResultURL\":\"http://your_result_url\",
    \"Occasion\":\" \"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest")
    .post(body)
    .addHeader("authorization", "Bearer YOUR_OAUTH_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    // Sample M-Pesa Core response received on the callback url.
  {
      "Result":{
      "ResultType":0,
      "ResultCode":0,
      "ResultDesc":"The service request has been accepted successfully.",
      "OriginatorConversationID":"19455-424535-1",
      "ConversationID":"AG_20170717_00006be9c8b5cc46abb6",
      "TransactionID":"LGH3197RIB",
      "ResultParameters":{
        "ResultParameter":[
          {
            "Key":"TransactionReceipt",
            "Value":"LGH3197RIB"
          },
          {
            "Key":"TransactionAmount",
            "Value":8000
          },
          {
            "Key":"B2CWorkingAccountAvailableFunds",
            "Value":150000
          },
          {
            "Key":"B2CUtilityAccountAvailableFunds",
            "Value":133568
          },
          {
            "Key":"TransactionCompletedDateTime",
            "Value":"17.07.2017 10:54:57"
          },
          {
            "Key":"ReceiverPartyPublicName",
            "Value":"254708374149 - John Doe"
          },
          {
            "Key":"B2CChargesPaidAccountAvailableFunds",
            "Value":0
          },
          {
            "Key":"B2CRecipientIsRegisteredCustomer",
            "Value":"Y"
          }
        ]
      },
      "ReferenceData":{
        "ReferenceItem":{
          "Key":"QueueTimeoutURL",
          "Value":"https://internalsandbox.safaricom.co.ke/mpesa/b2cresults/v1/submit"
        }
      }
    }
  }
  
This API enables Business to Customer (B2C) transactions between a company and customers who are the end-users of its products or services. Use of this API requires a valid and verified B2C M-Pesa Short code.

B2C Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest

B2C Query Parameters
Parameter	Description
InitiatorName	This is the credential/username used to authenticate the transaction request.
SecurityCredential	Base64 encoded string of the B2C short code and password, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.
CommandID	Unique command for each transaction type e.g. SalaryPayment, BusinessPayment, PromotionPayment
Amount	The amount being transacted
PartyA	Organization’s shortcode initiating the transaction.
PartyB	Phone number receiving the transaction
Remarks	Comments that are sent along with the transaction.
QueueTimeOutURL	The timeout end-point that receives a timeout response.
ResultURL	The end-point that receives the response of the transaction
Occasion	Optional
B2B API
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"Initiator\": \" \",
    \"SecurityCredential\": \" \",
    \"CommandID\": \" \",
    \"SenderIdentifierType\": \" \",
    \"RecieverIdentifierType\": \" \",
    \"Amount\": \" \",
    \"PartyA\": \" \",
    \"PartyB\": \" \",
    \"AccountReference\": \" \",
    \"Remarks\": \" \",
    \"QueueTimeOutURL\": \"http://your_timeout_url\",
    \"ResultURL\": \"http://your_result_url\"
  }" "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"Initiator\": \" \",
        \"SecurityCredential\": \" \",
        \"CommandID\": \" \",
        \"SenderIdentifierType\": \" \",
        \"RecieverIdentifierType\": \" \",
        \"Amount\": \" \",
        \"PartyA\": \" \",
        \"PartyB\": \" \",
        \"AccountReference\": \" \",
        \"Remarks\": \" \",
        \"QueueTimeOutURL\": \"http://your_timeout_url\",
        \"ResultURL\": \"http://your_result_url\"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "Initiator": " ",
    "SecurityCredential": " ",
    "CommandID": " ",
    "SenderIdentifierType": " ",
    "RecieverIdentifierType": " ",
    "Amount": " ",
    "PartyA": " ",
    "PartyB": " ",
    "AccountReference": " ",
    "Remarks": " ",
    "QueueTimeOutURL": "http://your_timeout_url",
    "ResultURL": "http://your_result_url"
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
      json : {
        "Initiator": " ",
        "SecurityCredential": " ",
        "CommandID": " ",
        "SenderIdentifierType": " ",
        "RecieverIdentifierType": " ",
        "Amount": " ",
        "PartyA": " ",
        "PartyB": " ",
        "AccountReference": " ",
        "Remarks": " ",
        "QueueTimeOutURL": "http://your_timeout_url",
        "ResultURL": "http://your_result_url"
      }
    },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'Initiator' => ' ',
    'SecurityCredential' => ' ',
    'CommandID' => ' ',
    'SenderIdentifierType' => ' ',
    'RecieverIdentifierType' => ' ',
    'Amount' => ' ',
    'PartyA' => ' ',
    'PartyB' => ' ',
    'AccountReference' => ' ',
    'Remarks' => ' ',
    'QueueTimeOutURL' => 'http://your_timeout_url',
    'ResultURL' => 'http://your_result_url'
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :Initiator ""
        :SecurityCredential ""
        :CommandID ""
        :SenderIdentifierType ""
        :RecieverIdentifierType ""
        :Amount ""
        :PartyA ""
        :PartyB ""
        :AccountReference ""
        :Remarks ""
        :QueueTimeOutURL "http://your_timeout_url"
        :ResultURL "http://your_result_url"
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"Initiator\": \" \",
        \"SecurityCredential\": \" \",
        \"CommandID\": \" \",
        \"SenderIdentifierType\": \" \",
        \"RecieverIdentifierType\": \" \",
        \"Amount\": \" \",
        \"PartyA\": \" \",
        \"PartyB\": \" \",
        \"AccountReference\": \" \",
        \"Remarks\": \" \",
        \"QueueTimeOutURL\": \"http://your_timeout_url\",
        \"ResultURL\": \"http://your_result_url\"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    {
    "Result":{
      "ResultType":0,
      "ResultCode":0,
      "ResultDesc":"The service request has been accepted successfully.",
      "OriginatorConversationID":"8551-61996-3",
      "ConversationID":"AG_20170727_00006baee344f4ce0796",
      "TransactionID":"LGR519G2QV",
      "ResultParameters":{
        "ResultParameter":[
          {
            "Key":"InitiatorAccountCurrentBalance",
            "Value":"{ Amount={BasicAmount=46713.00, MinimumAmount=4671300, CurrencyCode=KES}}"
          },
          {
            "Key":"DebitAccountCurrentBalance",
            "Value":"{Amount={BasicAmount=46713.00, MinimumAmount=4671300, CurrencyCode=KES}}"
          },
          {
            "Key":"Amount",
            "Value":10
          },
          {
            "Key":"DebitPartyAffectedAccountBalance",
            "Value":"Working Account|KES|46713.00|46713.00|0.00|0.00"
          },
          {
            "Key":"TransCompletedTime",
            "Value":20170727102524
          },
          {
            "Key":"DebitPartyCharges",
            "Value":"Business Pay Bill Charge|KES|77.00"
          },
          {
            "Key":"ReceiverPartyPublicName",
            "Value":"603094 - Safaricom3117"
          },
          {
            "Key":"Currency",
            "Value":"KES"
          }
        ]
      },
      "ReferenceData":{
        "ReferenceItem":[
          {
            "Key":"BillReferenceNumber",
            "Value":"aaa"
          },
          {
            "Key":"QueueTimeoutURL",
            "Value":"https://internalsandbox.safaricom.co.ke/mpesa/b2bresults/v1/submit"
          },
          {
            "Key":"Occasion"
          }
        ]
      }
    }
  }
  
This API enables Business to Business (B2B) transactions between a business and another business. Use of this API requires a valid and verified B2B M-Pesa short code for the business initiating the transaction and the both businesses involved in the transaction.

B2B - Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest

B2B - Request Parameters
Parameter	Description
Initiator	This is the credential/username used to authenticate the transaction request.
SecurityCredential	Base64 encoded string of the B2B short code and password, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.
CommandID	Unique command for each transaction type, possible values are: BusinessPayBill, MerchantToMerchantTransfer, MerchantTransferFromMerchantToWorking, MerchantServicesMMFAccountTransfer, AgencyFloatAdvance
Amount	The amount being transacted.
PartyA	Organization’s short code initiating the transaction.
SenderIdentifier	Type of organization sending the transaction.
PartyB	Organization’s short code receiving the funds being transacted.
RecieverIdentifierType	Type of organization receiving the funds being transacted.
Remarks	Comments that are sent along with the transaction.
QueueTimeOutURL	The path that stores information of time out transactions.it should be properly validated to make sure that it contains the port, URI and domain name or publicly available IP.
ResultURL	The path that receives results from M-Pesa it should be properly validated to make sure that it contains the port, URI and domain name or publicly available IP.
AccountReference	Account Reference mandatory for “BusinessPaybill” CommandID.
B2B Response Parameters
Parameter	Description
ConversationID	A unique numeric code generated by the M-Pesa system of the response to a request.
OriginatorConversationID	A unique numeric code generated by the M-Pesa system of the request.
ResponseDescription	A response message from the M-Pesa system accompanying the response to a request.
C2B API
This API enables Paybill and Buy Goods merchants to integrate to M-Pesa and receive real time payments notifications.

Register URL
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
      \"ShortCode\":\" \",
      \"ResponseType\":\" \",
      \"ConfirmationURL\":\"http://ip_address:port/confirmation\",
      \"ValidationURL\":\"http://ip_address:port/validation_url\"
  }" "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl')
  
  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(url)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"ShortCode\":\"ShortCode\",
      \"ResponseType\":\"ResponseType\",
      \"ConfirmationURL\":\"http://ip_address:port/confirmation\",
      \"ValidationURL\":\"http://ip_address:port/validation_url\"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "ShortCode": " ",
      "ResponseType": " ",
      "ConfirmationURL": "http://ip_address:port/confirmation",
      "ValidationURL": "http://ip_address:port/validation_url"}
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
        json : {
          "ShortCode": " ",
          "ResponseType": " ",
          "ConfirmationURL": "http://ip_address:port/confirmation",
          "ValidationURL": "http://ip_address:port/validation_url"
        }
      },
      function (error, response, body) {
        // TODO: Use the body object to extract the 
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'ShortCode' => ' ',
    'ResponseType' => ' ',
    'ConfirmationURL' => 'http://ip_address:port/confirmation',
    'ValidationURL' => 'http://ip_address:port/validation_url'
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]}
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :ShortCode ""
        :ResponseType ""
        :ConfirmationURL "http://ip_address:port/confirmation"
        :ValidationURL "http://ip_address:port/validation_url"
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"ShortCode\":\"ShortCode\",
      \"ResponseType\":\"ResponseType\",
      \"ConfirmationURL\":\"http://ip_address:port/confirmation\",
      \"ValidationURL\":\"http://ip_address:port/validation_url\"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
  
The C2B Register URL API registers the 3rd party’s confirmation and validation URLs to M-Pesa ; which then maps these URLs to the 3rd party shortcode. Whenever M-Pesa receives a transaction on the shortcode, M-Pesa triggers a validation request against the validation URL and the 3rd party system responds to M-Pesa with a validation response (either a success or an error code). The response expected is the success code the 3rd party

M-Pesa completes or cancels the transaction depending on the validation response it receives from the 3rd party system. A confirmation request of the transaction is then sent by M-Pesa through the confirmation URL back to the 3rd party which then should respond with a success acknowledging the confirmation.

The 3rd party resource URLs for both confirmation and validation must be HTTPS in production. Validation is an optional feature that needs to be activated on M-Pesa, the owner of the shortcode needs to make this request for activation.
C2B Register URL - Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl

C2B Register URL - Request Parameters
Parameter	Description
ValidationURL	Validation URL for the client.
ConfirmationURL	Confirmation URL for the client.
ResponseType	Default response type for timeout.
ShortCode	The short code of the organization.
Register URL - Response Parameters
Parameter	Description
ConversationID	A unique numeric code generated by the M-Pesa system of the response to a request.
OriginatorConversationID	A unique numeric code generated by the M-Pesa system of the request.
ResponseDescription	A response message from the M-Pesa system accompanying the response to a request.
C2B Simulate Transaction
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"ShortCode\":\" \",
    \"CommandID\":\"CustomerPayBillOnline\",
    \"Amount\":\" \",
    \"Msisdn\":\" \",
    \"BillRefNumber\":\" \"
  }" "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate')
  
  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(url)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{ \"ShortCode\":\" \",
    \"CommandID\":\"CustomerPayBillOnline\",
    \"Amount\":\" \",
    \"Msisdn\":\" \",
    \"BillRefNumber\":\" \" }"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "ACCESS_TOKEN"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "ShortCode":" ",
    "CommandID":"CustomerPayBillOnline",
    "Amount":" ",
    "Msisdn":" ",
    "BillRefNumber":" " }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
        json : {
          //Fill in the request parameters with valid values
          "ShortCode":" ",
          "CommandID":"CustomerPayBillOnline",
          "Amount":" ",
          "Msisdn":" ",
          "BillRefNumber":" "
        }
      },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate';
  
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
    $curl_post_data = array(
            //Fill in the request parameters with valid values
           'ShortCode' => ' ',
           'CommandID' => 'CustomerPayBillOnline',
           'Amount' => ' ',
           'Msisdn' => ' ',
           'BillRefNumber' => '00000'
    );
  
    $data_string = json_encode($curl_post_data);
  
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
    $curl_response = curl_exec($curl);
    print_r($curl_response);
  
    echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :ShortCode ""
        :CommandID "CustomerPayBillOnline"
        :Amount ""
        :Msisdn ""
        :BillRefNumber ""
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"ShortCode\":\" \",
    \"CommandID\":\"CustomerPayBillOnline\",
    \"Amount\":\" \",
    \"Msisdn\":\" \",
    \"BillRefNumber\":\" \" }");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    // Validation Response
  {
    "TransactionType":"",
    "TransID":"LGR219G3EY",
    "TransTime":"20170727104247",
    "TransAmount":"10.00",
    "BusinessShortCode":"600134",
    "BillRefNumber":"xyz",
    "InvoiceNumber":"",
    "OrgAccountBalance":"",
    "ThirdPartyTransID":"",
    "MSISDN":"254708374149",
    "FirstName":"John",
    "MiddleName":"Doe",
    "LastName":""
  }
  
  //Confirmation Respose
  {
    "TransactionType":"",
    "TransID":"LGR219G3EY",
    "TransTime":"20170727104247",
    "TransAmount":"10.00",
    "BusinessShortCode":"600134",
    "BillRefNumber":"xyz",
    "InvoiceNumber":"",
    "OrgAccountBalance":"49197.00",
    "ThirdPartyTransID":"1234567890",
    "MSISDN":"254708374149",
    "FirstName":"John",
    "MiddleName":"",
    "LastName":""
  }
  
C2B Simulate Transaction - Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate

C2B Simulate Transaction - Request Parameters
Parameter	Description
CommandID	Unique command for each transaction type.
Amount	The amount been transacted.
MSISDN	MSISDN (phone number) sending the transaction, start with country code without the plus(+) sign.
BillRefNumber	Bill Reference Number (Optional).
ShortCode	6 digit M-Pesa Till Number or PayBill Number
C2B Simulate Transaction - Response Parameters
Parameter	Description
ConversationID	A unique numeric code generated by the M-Pesa system of the response to a request.
OriginatorConversationID	A unique numeric code generated by the M-Pesa system of the request.
ResponseDescription	A response message from the M-Pesa system accompanying the response to a request.
Account Balance API
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
      \"Initiator\":\"Initiator\",
      \"SecurityCredential\":\"security credential\",
      \"CommandID\":\"AccountBalance\",
      \"PartyA\":\"shortcode\",
      \"IdentifierType\":\"4\",
      \"Remarks\":\"Remarks\",
      \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
      \"ResultURL\":\"https://ip_address:port/result_url\"
  }" "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"Initiator\":\" \",
      \"SecurityCredential\":\" \",
      \"CommandID\":\"AccountBalance\",
      \"PartyA\":\" \",
      \"IdentifierType\":\"4\",
      \"Remarks\":\" \",
      \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
      \"ResultURL\":\"https://ip_address:port/result_url\"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "Initiator":" ",
      "SecurityCredential":" ",
      "CommandID":"AccountBalance",
      "PartyA":"shortcode",
      "IdentifierType":"4",
      "Remarks":"Remarks",
      "QueueTimeOutURL":"https://ip_address:port/timeout_url",
      "ResultURL":"https://ip_address:port/result_url"
      }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
        json : {
          "Initiator":" ",
          "SecurityCredential":" ",
          "CommandID":"AccountBalance",
          "PartyA":" ",
          "IdentifierType":"4",
          "Remarks":" ",
          "QueueTimeOutURL":"https://ip_address:port/timeout_url",
          "ResultURL":"https://ip_address:port/result_url"
          }
      },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'CommandID' => ' ',
    'Initiator' => ' ',
    'SecurityCredential' => ' ',
    'CommandID' => 'AccountBalance',
    'PartyA' => ' ',
    'IdentifierType' => '4',
    'Remarks' => ' ',
    'QueueTimeOutURL' => 'https://ip_address:port/timeout_url',
    'ResultURL' => 'https://ip_address:port/result_url'
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :Initiator ""
        :SecurityCredential ""
        :CommandID "AccountBalance"
        :PartyA ""
        :IdentifierType "4"
        :Remarks ""
        :QueueTimeOutURL "https://ip_address:port/timeout_url"
        :ResultURL "https://ip_address:port/result_url"
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"Initiator\":\" \",
      \"SecurityCredential\":\" \",
      \"CommandID\":\"AccountBalance\",
      \"PartyA\":\" \",
      \"IdentifierType\":\"4\",
      \"Remarks\":\" \",
      \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
      \"ResultURL\":\"https://ip_address:port/result_url\"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    {
    "Result":{
      "ResultType":0,
      "ResultCode":0,
      "ResultDesc":"The service request has b een accepted successfully.",
      "OriginatorConversationID":"19464-802673-1",
      "ConversationID":"AG_20170728_0000589b6252f7f25488",
      "TransactionID":"LGS0000000",
      "ResultParameters":{
        "ResultParameter":[
          {
            "Key":"AccountBalance",
            "Value":"Working Account|KES|46713.00|46713.00|0.00|0.00&Float Account|KES|0.00|0.00|0.00|0.00&Utility Account|KES|49217.00|49217.00|0.00|0.00&Charges Paid Account|KES|-220.00|-220.00|0.00|0.00&Organization Settlement Account|KES|0.00|0.00|0.00|0.00"
          },
          {
            "Key":"BOCompletedTime",
            "Value":20170728095642
          }
        ]
      },
      "ReferenceData":{
        "ReferenceItem":{
          "Key":"QueueTimeoutURL",
          "Value":"https://internalsandbox.safaricom.co.ke/mpesa/abresults/v1/submit"
        }
      }
    }
  }
  
The Account Balance API requests for the account balance of a shortcode.

Account Balance - Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query

Account Balance - Request Parameters
Parameter	Description
Initiator	This is the credential/username used to authenticate the transaction request.
SecurityCredential	Base64 encoded string of the M-Pesa short code and password, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.
CommandID	A unique command passed to the M-Pesa system.
PartyB	The shortcode of the organisation receiving the transaction.
ReceiverIdentifierType	Type of the organisation receiving the transaction.
Remarks	Comments that are sent along with the transaction.
QueueTimeOutURL	The timeout end-point that receives a timeout message.
ResultURL	The end-point that receives a successful transaction.
AccountType	Organisation receiving the funds.
Transaction Status
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"Initiator\": \" \",
    \"SecurityCredential\": \" \",
    \"CommandID\":\"TransactionStatusQuery\",
    \"TransactionID\": \" \",
    \"PartyA\": \" \",
    \"IdentifierType\":\"1\",
    \"ResultURL\":\"https://ip_address:port/result_url\",
    \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
    \"Remarks\": \" \",
    \"Occasion\": \" \"
  }" "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"Initiator\": \" \",
    \"SecurityCredential\": \" \",
    \"CommandID\":\"TransactionStatusQuery\",
    \"TransactionID\": \" \",
    \"PartyA\": \" \",
    \"IdentifierType\":\"1\",
    \"ResultURL\":\"https://ip_address:port/result_url\",
    \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
    \"Remarks\": \" \",
    \"Occasion\": \" \"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "Initiator":" ",
    "SecurityCredential":" ",
    "CommandID":"TransactionStatusQuery",
    "TransactionID":" ",
    "PartyA":" ",
    "IdentifierType":"1",
    "ResultURL":"https://ip_address:port/result_url",
    "QueueTimeOutURL":"https://ip_address:port/timeout_url",
    "Remarks":" ",
    "Occasion":" "
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
      json : {
        "Initiator":" ",
        "SecurityCredential":" ",
        "CommandID":"TransactionStatusQuery",
        "TransactionID":" ",
        "PartyA":" ",
        "IdentifierType":"1",
        "ResultURL":"https://ip_address:port/result_url",
        "QueueTimeOutURL":"https://ip_address:port/timeout_url",
        "Remarks":" ",
        "Occasion":" "
      }
    },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'Initiator' => ' ',
    'SecurityCredential' => ' ',
    'CommandID' => 'TransactionStatusQuery',
    'TransactionID' => ' ',
    'PartyA' => ' ',
    'IdentifierType' => '1',
    'ResultURL' => 'https://ip_address:port/result_url',
    'QueueTimeOutURL' => 'https://ip_address:port/timeout_url',
    'Remarks' => ' ',
    'Occasion' => ' '
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :Initiator ""
        :SecurityCredential ""
        :CommandID "TransactionStatusQuery"
        :TransactionID "" 
        :PartyA "" 
        :IdentifierType "1"
        :ResultURL "https://ip_address:port/result_url"
        :QueueTimeOutURL "https://ip_address:port/timeout_url"
        :Remarks ""
        :Occasion ""
        })
    })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"Initiator\": \" \",
    \"SecurityCredential\": \" \",
    \"CommandID\":\"TransactionStatusQuery\",
    \"TransactionID\": \" \",
    \"PartyA\": \" \",
    \"IdentifierType\":\"1\",
    \"ResultURL\":\"https://ip_address:port/result_url\",
    \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
    \"Remarks\": \" \",
    \"Occasion\": \" \"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    {
    "Result":{
      "ResultType":0,
      "ResultCode":0,
      "ResultDesc":"The service request has been accepted successfully.",
      "OriginatorConversationID":"10816-694520-2",
      "ConversationID":"AG_20170727_000059c52529a8e080bd",
      "TransactionID":"LGR0000000",
      "ResultParameters":{
        "ResultParameter":[
          {
            "Key":"ReceiptNo",
            "Value":"LGR919G2AV"
          },
          {
            "Key":"Conversation ID",
            "Value":"AG_20170727_00004492b1b6d0078fbe"
          },
          {
            "Key":"FinalisedTime",
            "Value":20170727101415
          },
          {
            "Key":"Amount",
            "Value":10
          },
          {
            "Key":"TransactionStatus",
            "Value":"Completed"
          },
          {
            "Key":"ReasonType",
            "Value":"Salary Payment via API"
          },
          {
            "Key":"TransactionReason"
          },
          {
            "Key":"DebitPartyCharges",
            "Value":"Fee For B2C Payment|KES|33.00"
          },
          {
            "Key":"DebitAccountType",
            "Value":"Utility Account"
          },
          {
            "Key":"InitiatedTime",
            "Value":20170727101415
          },
          {
            "Key":"Originator Conversation ID",
            "Value":"19455-773836-1"
          },
          {
            "Key":"CreditPartyName",
            "Value":"254708374149 - John Doe"
          },
          {
            "Key":"DebitPartyName",
            "Value":"600134 - Safaricom157"
          }
        ]
      },
      "ReferenceData":{
        "ReferenceItem":{
          "Key":"Occasion",
          "Value":"aaaa"
        }
      }
    }
  }
  
Transaction Status API checks the status of a B2B, B2C and C2B APIs transactions.

Transaction Status Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query

Transaction Status Request Parameters
Parameter	Description
CommandID	Unique command for each transaction type, possible values are: TransactionStatusQuery.
ShortCode	Organization /MSISDN sending the transaction.
IdentifierType	Type of organization receiving the transaction
Remarks	Comments that are sent along with the transaction.
Initiator	The name of Initiator to initiating the request.
SecurityCredential	Base64 encoded string of the M-Pesa short code and password, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.
QueueTimeOutURL	The path that stores information of time out transaction.
ResultURL	The path that stores information of transaction.
TransactionID	Organization Receiving the funds.
Occasion	Optional.
Reversal
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"Initiator\":\" \",
    \"SecurityCredential\":\" \",
    \"CommandID\":\"TransactionReversal\",
    \"TransactionID\":\" \",
    \"Amount\":\" \",
    \"ReceiverParty\":\" \",
    \"RecieverIdentifierType\":\"4\",
    \"ResultURL\":\"https://ip_address:port/result_url\",
    \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
    \"Remarks\":\" \",
    \"Occasion\":\" \"
  }" "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"Initiator\":\" \",
    \"SecurityCredential\":\" \",
    \"CommandID\":\"TransactionReversal\",
    \"TransactionID\":\" \",
    \"Amount\":\" \",
    \"ReceiverParty\":\" \",
    \"RecieverIdentifierType\":\"4\",
    \"ResultURL\":\"https://ip_address:port/result_url\",
    \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
    \"Remarks\":\" \",
    \"Occasion\":\" \"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "Initiator":" ",
    "SecurityCredential":" ",
    "CommandID":"TransactionReversal",
    "TransactionID":" ",
    "Amount":" ",
    "ReceiverParty":" ",
    "RecieverIdentifierType":"4",
    "ResultURL":"https://ip_address:port/result_url",
    "QueueTimeOutURL":"https://ip_address:port/timeout_url",
    "Remarks":" ",
    "Occasion":" "
    }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
        json : {
          "Initiator":" ",
          "SecurityCredential":" ",
          "CommandID":"TransactionReversal",
          "TransactionID":" ",
          "Amount":" ",
          "ReceiverParty":" ",
          "RecieverIdentifierType":"4",
          "ResultURL":"https://ip_address:port/result_url",
          "QueueTimeOutURL":"https://ip_address:port/timeout_url",
          "Remarks":" ",
          "Occasion":" "
          }
      },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'CommandID' => ' ',
    'Initiator' => ' ',
    'SecurityCredential' => ' ',
    'CommandID' => 'TransactionReversal',
    'TransactionID' => ' ',
    'Amount' => ' ',
    'ReceiverParty' => ' ',
    'RecieverIdentifierType' => '4',
    'ResultURL' => 'https://ip_address:port/result_url',
    'QueueTimeOutURL' => 'https://ip_address:port/timeout_url',
    'Remarks' => ' ',
    'Occasion' => ' '
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :Initiator ""
        :SecurityCredential ""
        :CommandID "TransactionReversal"
        :TransactionID ""
        :Amount ""
        :ReceiverParty ""
        :RecieverIdentifierType "4"
        :ResultURL "https://ip_address:port/result_url"
        :QueueTimeOutURL "https://ip_address:port/timeout_url"
        :Remarks ""
        :Occasion ""
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"Initiator\":\" \",
    \"SecurityCredential\":\" \",
    \"CommandID\":\"TransactionReversal\",
    \"TransactionID\":\" \",
    \"Amount\":\" \",
    \"ReceiverParty\":\" \",
    \"RecieverIdentifierType\":\"4\",
    \"ResultURL\":\"https://ip_address:port/result_url\",
    \"QueueTimeOutURL\":\"https://ip_address:port/timeout_url\",
    \"Remarks\":\" \",
    \"Occasion\":\" \"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    {
    "Result":{
      "ResultType":0,
      "ResultCode":0,
      "ResultDesc":"The service request has been accepted successfully.",
      "OriginatorConversationID":"10819-695089-1",
      "ConversationID":"AG_20170727_00004efadacd98a01d15",
      "TransactionID":"LGR019G3J2",
      "ReferenceData":{
        "ReferenceItem":{
          "Key":"QueueTimeoutURL",
          "Value":"https://internalsandbox.safaricom.co.ke/mpesa/reversalresults/v1/submit"
        }
      }
    }
  }
  
Reverses a B2B, B2C or C2B M-Pesa transaction.

Reversal Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request

Reversal Request Parameters
Parameter	Description
Initiator	This is the credential/username used to authenticate the transaction request.
SecurityCredential	Base64 encoded string of the M-Pesa short code and password, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.
CommandID	Unique command for each transaction type, possible values are: TransactionReversal.
PartyA	Organization/MSISDN sending the transaction.
RecieverIdentifierType	Type of organization receiving the transaction.
Remarks	Comments that are sent along with the transaction.
QueueTimeOutURL	The path that stores information of time out transaction.
ResultURL	The path that stores information of transaction.
TransactionID	Organization Receiving the funds.
Occasion	Optional.
Lipa na M-Pesa Online Payment
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"BusinessShortCode\": \" \",
    \"Password\": \" \",
    \"Timestamp\": \" \",
    \"TransactionType\": \"CustomerPayBillOnline\",
    \"Amount\": \" \",
    \"PartyA\": \" \",
    \"PartyB\": \" \",
    \"PhoneNumber\": \" \",
    \"CallBackURL\": \"https://ip_address:port/callback\",
    \"AccountReference\": \" \",
    \"TransactionDesc\": \" \"
  }" "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"BusinessShortCode\": \" \",
    \"Password\": \" \",
    \"Timestamp\": \" \",
    \"TransactionType\": \"CustomerPayBillOnline\",
    \"Amount\": \" \",
    \"PartyA\": \" \",
    \"PartyB\": \" \",
    \"PhoneNumber\": \" \",
    \"CallBackURL\": \"https://ip_address:port/callback\",
    \"AccountReference\": \" \",
    \"TransactionDesc\": \" \"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "BusinessShortCode": " ",
    "Password": " ",
    "Timestamp": " ",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": " ",
    "PartyA": " ",
    "PartyB": " ",
    "PhoneNumber": " ",
    "CallBackURL": "https://ip_address:port/callback",
    "AccountReference": " ",
    "TransactionDesc": " "
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
      json : {
        "BusinessShortCode": " ",
        "Password": " ",
        "Timestamp": " ",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": " ",
        "PartyA": " ",
        "PartyB": " ",
        "PhoneNumber": " ",
        "CallBackURL": "https://ip_address:port/callback",
        "AccountReference": " ",
        "TransactionDesc": " "
      }
    },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'BusinessShortCode' => ' ',
    'Password' => ' ',
    'Timestamp' => ' ',
    'TransactionType' => 'CustomerPayBillOnline',
    'Amount"' => ' ',
    'PartyA' => ' ',
    'PartyB' => ' ',
    'PhoneNumber' => ' ',
    'CallBackURL' => 'https://ip_address:port/callback',
    'AccountReference' => ' ',
    'TransactionDesc' => ' '
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :BusinessShortCode ""
        :Password ""
        :Timestamp ""
        :TransactionType "CustomerPayBillOnline"
        :Amount ""
        :PartyA ""
        :PartyB ""
        :PhoneNumber "" 
        :CallBackURL "https://ip_address:port/callback"
        :AccountReference ""
        :TransactionDesc ""
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"BusinessShortCode\": \" \",
    \"Password\": \" \",
    \"Timestamp\": \" \",
    \"TransactionType\": \"CustomerPayBillOnline\",
    \"Amount\": \" \",
    \"PartyA\": \" \",
    \"PartyB\": \" \",
    \"PhoneNumber\": \" \",
    \"CallBackURL\": \"https://ip_address:port/callback\",
    \"AccountReference\": \" \",
    \"TransactionDesc\": \" \"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    // A cancelled request
  {
    "Body":{
      "stkCallback":{
        "MerchantRequestID":"8555-67195-1",
        "CheckoutRequestID":"ws_CO_27072017151044001",
        "ResultCode":1032,
        "ResultDesc":"[STK_CB - ]Request cancelled by user"
      }
    }
  }
  
  // An accepted request
  {
    "Body":{
      "stkCallback":{
        "MerchantRequestID":"19465-780693-1",
        "CheckoutRequestID":"ws_CO_27072017154747416",
        "ResultCode":0,
        "ResultDesc":"The service request is processed successfully.",
        "CallbackMetadata":{
          "Item":[
            {
              "Name":"Amount",
              "Value":1
            },
            {
              "Name":"MpesaReceiptNumber",
              "Value":"LGR7OWQX0R"
            },
            {
              "Name":"Balance"
            },
            {
              "Name":"TransactionDate",
              "Value":20170727154800
            },
            {
              "Name":"PhoneNumber",
              "Value":254721566839
            }
          ]
        }
      }
    }
  }
  
Lipa na M-Pesa Online Payment API is used to initiate a M-Pesa transaction on behalf of a customer using STK Push. This is the same technique mySafaricom App uses whenever the app is used to make payments.

Lipa na M-Pesa Online Payment - Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest

Lipa na M-Pesa Online Payment - Request Parameters
Parameter	Description
BusinessShortCode	The organization shortcode used to receive the transaction.
Password	The password for encrypting the request. This is generated by base64 encoding BusinessShortcode, Passkey and Timestamp.
Timestamp	The timestamp of the transaction in the format yyyymmddhhiiss.
TransactionType	The transaction type to be used for this request. Only CustomerPayBillOnline is supported.
Amount	The amount to be transacted.
PartyA	The MSISDN sending the funds.
PartyB	The organization shortcode receiving the funds
PhoneNumber	The MSISDN sending the funds.
CallBackURL	The url to where responses from M-Pesa will be sent to.
AccountReference	Used with M-Pesa PayBills.
TransactionDesc	A description of the transaction.
Lipa na M-Pesa Online Payment - Response Parameters
Parameter	Description
MerchantRequestID	Merchant Request ID
CheckoutRequestID	Check out Request ID
ResponseCode	Response Code
ResultDesc	Result Desc
ResponseDescription	Response Description message
ResultCode	Result Code
Lipa na M-Pesa Online Query Request
  curl -X POST --header "Authorization: Bearer <Access-Token>" --header "Content-Type: application/json" -d "{
    \"BusinessShortCode\":\" \" ,
    \"Password\":\" \",
    \"Timestamp\":\" \",
    \"CheckoutRequestID\":\" \"
  }" "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
  
    require 'net/http'
  require 'net/https'
  require 'uri'
  
  uri = URI('https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query')
  
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_NONE
  
  request = Net::HTTP::Get.new(uri)
  request["accept"] = 'application/json'
  request["content-type"] = 'application/json'
  request["authorization"] = 'Bearer <Access-Token>'
  request.body = "{\"BusinessShortCode\":\" \" ,
          \"Password\":\" \",
          \"Timestamp\":\" \",
          \"CheckoutRequestID\":\" \"}"
  
  response = http.request(request)
  puts response.read_body
    import requests
  
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "BusinessShortCode": " " ,
          "Password": " ",
          "Timestamp": " ",
          "CheckoutRequestID": " "
    }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
    var request = require('request'),
    oauth_token = "ACCESS_TOKEN",
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
    auth = "Bearer " + oauth_token;
  
    request(
      {
        method: 'POST'
        url : url,
        headers : {
          "Authorization" : auth
        },
        json : {
          "BusinessShortCode": " " ,
          "Password": " ",
          "Timestamp": " ",
          "CheckoutRequestID": " "
          }
      },
      function (error, response, body) {
        // TODO: Use the body object to extract the response
        console.log(body)
      }
    )
    <?php
  $url = 'https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query';
  
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer ACCESS_TOKEN')); //setting custom header
  
  
  $curl_post_data = array(
    //Fill in the request parameters with valid values
    'BusinessShortCode' => ' ',
    'Password' => ' ',
    'Timestamp' => ' ',
    'CheckoutRequestID' => ' '
  );
  
  $data_string = json_encode($curl_post_data);
  
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_POST, true);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $data_string);
  
  $curl_response = curl_exec($curl);
  print_r($curl_response);
  
  echo $curl_response;
  ?>
    (let[
    {:keys [body]} 
    (clj-http.client/post "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"{
      :headers {"Content-Type" "application/json"}
      :oauth-token "ACCESS_TOKEN"
      :body (clojure.data.json/write-str {
        :BusinessShortCode "" 
        :Password ""
        :Timestamp ""
        :CheckoutRequestID ""
        })
      })
    ]
    (json/read-str body :key-fn keyword)
  )
    OkHttpClient client = new OkHttpClient();
  
  MediaType mediaType = MediaType.parse("application/json");
  RequestBody body = RequestBody.create(mediaType, "{\"BusinessShortCode\":\" \" ,
          \"Password\":\" \",
          \"Timestamp\":\" \",
          \"CheckoutRequestID\":\" \"}");
  Request request = new Request.Builder()
    .url("https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query")
    .post(body)
    .addHeader("authorization", "Bearer ACCESS_TOKEN")
    .addHeader("content-type", "application/json")
    .build();
  
  Response response = client.newCall(request).execute();
    {
    "ResponseCode":"0",
    "ResponseDescription":"The service request has been accepted successfully",
    "MerchantRequestID":"8555-67195-1",
    "CheckoutRequestID":"ws_CO_27072017151044001",
    "ResultCode":"1032",
    "ResultDesc":"[STK_CB - ]Request cancelled by user"
  }
  
Lipa na M-Pesa Online Query Request - Resource URL
POST https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query

Lipa na M-Pesa Online Query Request - Request Parameters
Parameter	Description
BusinessShortCode	Business Short Code
Password	Password
Timestamp	Timestamp
CheckoutRequestID	Checkout RequestID
Lipa na M-Pesa Online Query Request - Response Parameters
Parameter	Description
MerchantRequestID	Merchant Request ID
CheckoutRequestID	Check out Request ID
ResponseCode	Response Code
ResultDesc	Result Desc
ResponseDescription	Response Description message
ResultCode	Result Code
Errors