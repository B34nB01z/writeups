use rand::{Rng,SeedableRng};
use rand::rngs::StdRng;
use std::{fs,str};
use std::io::Write;
use hex::decode;

fn get_rng() -> StdRng {
    let seed = 13371337;
    return StdRng::seed_from_u64(seed);
}

fn rand_xor(input : Vec<u8>) -> String {
    let mut rng = get_rng();
    return input
        .into_iter()
        .map(|c| format!("{:02x}", (c as u8 ^ rng.gen::<u8>())))
        .collect::<Vec<String>>()
        .join("");
}

fn main() -> std::io::Result<()> {
    let tmp = hex::decode(fs::read_to_string("../out.txt")?).expect("pls dont crash");
    let flag = rand_xor(tmp);
    println!("{}", String::from_utf8(hex::decode(flag).expect("no crash por favor")).expect("no CRASH"));
    Ok(())
}
