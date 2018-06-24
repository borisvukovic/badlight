#define NUMBER_OF_LIGHTS 6

char state[] = "nnnnnn";
char command = 'c';
int argument = -1;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  while(get_command() != 1);

  //Recieved command
  bool valid_command = check_command(command, argument);
  send_ack_nack(valid_command);
  if(valid_command) {
    execute_command();
  }
}

int get_command() {
  while(Serial.available()) {
    // Let the buffer fill up
    delay(50);
    // Check for start character for command
    if((char)Serial.read() == '#') {
      command = (char)Serial.read();
      argument = convert_to_int((char)Serial.read());
      return 1;
    }
  }
  return 0;
}

bool check_command(char command, int argument) {
  return (argument >= 0 && argument <= 5) && (command == 'a' || command == 'd' || command == 'i' || command == 'r');
}

void execute_command() {
  bool err = false;
  switch(command) {
    case 'a':
      //activate light
      if(activate_light(argument) != 0) {
        err = true;
      }
      break;
    case 'i':
      //init light
      if(init_light(argument) != 0) {
        err = true;
      }
      break;
    case 'd':
      //deactivate light
      if(deactivate_light(argument) != 0) {
        err = true;
      }
      break;
    case 'r':
      //reset all
      err = false;
      break;
    default:
      err = true;
      break;
  }
  send_err_ok(err);
}

void send_ack_nack(bool ack) {
  if(ack) {
    Serial.println("ACK");
  } else {
    Serial.println("NACK");
  }
}

void send_err_ok(bool err) {
  if(err) {
    Serial.println("ERR");
  } else {
    Serial.println("OK");
  }
}

int activate_light(int address) {
  digitalWrite(LED_BUILTIN, HIGH);
  return 0;
}

int deactivate_light(int address) {
  digitalWrite(LED_BUILTIN, LOW);
  return 0;
}

int init_light(int address) {
  return 0;
}

int convert_to_int(char c) {
  return (int)c - 48;
}