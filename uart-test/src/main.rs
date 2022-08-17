use rust_uart::*;
use serial::*;
use std::time::Duration;

const TIMEOUT: Duration = Duration::from_millis(50);

fn main() {
    let settings = serial::PortSettings{
        baud_rate: Baud115200,
        char_size: Bits8,
        parity: ParityNone,
        stop_bits: Stop1,
        flow_control: FlowNone,
    };
    let uart = Connection::from_path("/dev/ttyS0",settings,TIMEOUT).unwrap();

    let msg = [0,1];

    match uart.write(&msg) {
        Ok(()) => {
            loop {
                match uart.read(2,TIMEOUT) {
                    Ok(b) => {
                        if b == [1,0] {
                            println!("Success");
                            break;
                        }
                        else {
                            println!("{:?}",b)
                        }
                    }
                    _ => continue
                }
            }
        }
        Err(_) => println!("Failed to send")
    }
}
