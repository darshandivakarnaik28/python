const students={
    ST101:{
        Name:"Rahul",
        department:"CSE",
        cgpa:8.4,
        backlogs:0,
        skills:["JavaScript","Python","SQL"],
        placement:{
            status:"Not Placed",
            company:null,
            package:0
        }
    },
    ST102:{
        Name:"Anita",
        department:"ISE",
        cgpa:9.1,
        backlogs:0,
        skills:["Java","SQL","React"],
        placement:{
            status:"Placed",
            company:"infosys",
            package:6.5
        }
    },
    ST103:{
        Name:"Kiran",
        department:"CSE",
        cgpa:7.2,
        backlogs:1,
        skills:["Python","SQL"],
        placement:{
            status:"Not Placed",
            company:null,
            package:0
        }
    },
    ST104:{
        Name:"Priya",
        department:"ECE",
        cgpa:8.8,
        backlogs:0,
        skills:["Python","EmbeddedC","SQL"],
        placement:{
            status:"Placed",
            company:"TCS",
            package:7.2
        }
    },
    ST105:{
        Name:"Arjun",
        department:"CSE",
        cgpa:8.0,
        backlogs:0,
        skills:["JavaScript","React","Node.js"],
        placement:{
            status:"Not Placed",
            company:null,
            package:0
        }
    },
    ST106:{
        Name:"Sneha",
        department:"ISE",
        cgpa:7.8,
        backlogs:0,
        skills:["Python","JavaScript","SQL"],
        placement:{
            status:"Not Placed",
            company:null,
            package:0
        }
    }
}

const companies={
    Infosys:{
        minimunCGPA:7.5,
        maximumBacklogs:0,
        requiredSkill:"SQL",
        package:6.5
    },

    TCS:{
        minimunCGPA:8.0,
        maximumBacklogs:0,
        requiredSkill:"Python",
        package:7.2
    },

    TechNova:{
        minimunCGPA:8.0,
        maximumBacklogs:0,
        requiredSkill:"JavaScript",
        package:10
    },

    DataWorks:{
        minimunCGPA:8.5,
        maximumBacklogs:0,
        requiredSkill:"Python",
        package:12
    },
};

function DisplayStudents(){
    let result="";
    for(const i in students){
        result+=`${i}\nName: ${students[i]["Name"]}\nDepartment: ${students[i]["department"]}\nCCGPA: ${students[i]["cgpa"]}\nBacklogs: ${students[i]["backlogs"]}\nStatus: ${students[i]["placement"]["status"]}\n\n`;
    }
    return result;
}

function search(sid){
    if(sid in students){
        return(`\nStudent Found\n${sid}\nName: ${students[sid]["Name"]}\nDepartment: ${students[sid]["department"]}\nCCGPA: ${students[sid]["cgpa"]}\nBacklogs: ${students[sid]["backlogs"]}\nStatus: ${students[sid]["placement"]["status"]}\n\n`);
    }
        else{
            
            return("Student Not Found");
        }
    }

function check_eligibility(stuid,companyname){
    console.log("============ELIGIBILITY RESULT================");
    let result="";
    let cgpa;
    let backlogs;
    let skills=[];
    let minCGPA;
    let maxbacklogs;
    let requiredskill;
    if(stuid in students && companyname in companies){
        cgpa=students[stuid]["cgpa"];
        backlogs=students[stuid]["backlogs"];
        skills=students[stuid]["skills"];
        minCGPA=companies[companyname]["minimunCGPA"];
        maxbacklogs=companies[companyname]["maximumBacklogs"];
        requiredskill=companies[companyname]["requiredSkill"];
    result+=`Student: ${students[stuid]["Name"]}\nCompany: ${companyname}\n`;
    if(cgpa>=minCGPA){
        result+="CGPA Requirements: PASSED\n";
    }
    else{
        result+="CGPA Requirements: FAILED\n";
    }

    if(backlogs<=maxbacklogs){
        result+="Backlogs Requirements: PASSED\n";
    }
    else{
        result+="Backlogs Requirements: FAILED\n";
    }

    if(skills.includes(requiredskill)){
        result+="Skills Requirement: PASSED\n";
    }
    else{
        result+="Skills Requirement: FAILED\n";
    }

    if(cgpa>=minCGPA && backlogs<=maxbacklogs && (skills.includes(requiredskill))){
        result+="RESULT: ELIGIBLE\n";
    }
    else{
        result+="RESULT: NOT ELIGIBLE\n";
    }
    return result;
}
else{
    return "Not Found";
}
}

function placedstudents(){
    let result="";
    for(const i in students){
        if((students[i]["placement"]["status"])==="Placed"){
            result+=`${students[i]["Name"]}\nCompany: ${students[i]["placement"]["company"]}\nPackage: ${students[i]["placement"]["package"]} LPA\n\n`;
        }

    }
    return result;
}

function notplacedstudents(){
    let result="";
    for (const i in students){
        if((students[i]["placement"]["status"])==="Not Placed"){
            result+=`${students[i]["Name"]}\nCompany: ${students[i]["placement"]["company"]}\nPackage: ${students[i]["placement"]["package"]} LPA\n\n`;
        }
    }
    return result;
}

function deparment_statistics(){
    let result="";
    const departments={
        CSE:{
            total:0,
            placed:0,
            unplaced:0,
            },
        ISE:{
            total:0,
            placed:0,
            unplaced:0
        },
        ECE:{
            total:0,
            placed:0,
            unplaced:0
        }
    }
    for(const i in students){
        if(students[i]["department"]==="CSE"){
            departments["CSE"]["total"]++;
            if(students[i]["placement"]["status"]==="Placed"){
                departments["CSE"]["placed"]++;
            }
            else{
               departments["CSE"]["unplaced"]++;
            }
            
        } 
        else if(students[i]["department"]==="ISE"){
            departments["ISE"]["total"]++;
            if(students[i]["placement"]["status"]==="Placed"){
                departments["ISE"]["placed"]++;
            }
            else{
               departments["ISE"]["unplaced"]++;
            }
            
        }
        else{
            departments["ECE"]["total"]++;
            if(students[i]["placement"]["status"]==="Placed"){
                departments["ECE"]["placed"]++;
            }
            else{
               departments["ECE"]["unplaced"]++;
            }
        }
    }
    for(const dep in departments){
        result+=`${dep}\nTotal: ${departments[dep]["total"]}\nPlaced: ${departments[dep]["placed"]}\nUnplaced: ${departments[dep]["unplaced"]}\n\n`;
    }        
return result;
}

function placement_statistics(){
    console.log("============PLACEMENT STATISTICS============");
    const placements={placed:0,unplaced:0};
    let total=0;
    let sum=0;
    let package=0;
    let max_package=0;
    for(const i in students){
        total++;
        sum+=students[i]["cgpa"];
        package+=students[i]["placement"]["package"];
        if(students[i]["placement"]["package"]>max_package){
            max_package=students[i]["placement"]["package"];
        }
        if(students[i]["placement"]["status"]==="Placed"){
            placements["placed"]++;
        }
        else{
            placements["unplaced"]++;
        }
    }
    const result=`Total Students :${total}\nPlaced Students :${placements["placed"]}\nUnplaced Students :${placements["unplaced"]}\nPlacement Rate :${(placements["placed"]/total)*100}\nAverage CGPA :${sum/total}\nAverage Package :${package/placements["placed"]} LPA\nHighest Package :${max_package} LPA`;
    return result;
}

function update_placement(sid,cname,package){
        if(sid in students){
                students[sid]["placement"]["company"]=cname;
                students[sid]["placement"]["package"]=package;
                students[sid]["placement"]["status"]="Placed";
                console.log("Placement Update Successfully "+students[sid]["Name"]+" is now placed at "+cname+" with a package of "+package+"LPA.");
        }
    }

function company_statistics(cname){
    console.log(`==============${cname} ELIGIBILITY==================`);
    if(cname in companies){
        let min=companies[cname]["minimunCGPA"];
        let max=companies[cname]["maximumBacklogs"];
        let skill=companies[cname]["requiredSkill"];
        let pack=companies[cname]["package"];
    let stu=[];
    for(const i in students){
        if(students[i]["cgpa"]>=min && students[i]["backlogs"]<=max && students[i]["skills"].includes(skill)){
            stu.push(students[i]["Name"]);
        }
    }
    console.log(`Minimum CGPA :${min}\n Maximum CGPA :${max}\nRequired Skill :${skill}\nPackage :${pack}\n\nEligible Students:\n`);
    for(let i=0;i<stu.length;i++){
        console.log(i+1,stu[i]);
    }
    console.log("Total Eligible Students:",stu.length);
}
}

function highest_package(){
    let max_pack=0;
    for(const i in students){
        if(students[i]["placement"]["package"]>max_pack){
            max_pack=students[i]["placement"]["package"];
        }
    }
    for(const i in students){
        if(max_pack===students[i]["placement"]["package"]){
            console.log(`Student: ${students[i]["Name"]}\nCompany:${students[i]["placement"]["company"]}\nPackage:${students[i]["placement"]["package"]}\n`);
        }
    }
    
}

function search_skill(skill){
    let count=0;
    console.log("===============STUDENTS WITH",skill,"===============");
    for(const i in students){
        for(let j of students[i]["skills"]){
            if(j===skill){
                count++;
                console.log(students[i]["Name"]);
            }

        }

    }
    console.log("Total:",count);
}

function above_CGPA(cgpa){
    let count=0;
    console.log("Studeents with CGPA>=",cgpa);
    for(const i in students){
        if(students[i]["cgpa"]>=cgpa){
            count++;
            console.log(students[i]["Name"],"-",students[i]["cgpa"],"\n");
        }
    }
    console.log("Total:",count);
}

   
        
while (true){
    console.log("====================CAMPUS PLACEMENT SYSTEM======================");
    console.log("0.Exit\n1.Display All Students\n2.Search Student\n3.Check Company Eligibility\n4.Display Placed Students\n5.Display Unplaced Students\n6.Department Statics\n7.Placement Statistics\n8.Update Placement\n9.Company-wise Eligible Students\n10.Highest Package\n11.Search By Skill\n12.Student Above CGPA\n");
    let choice=Number(prompt("Enter a choice:"));
    if(choice===1){
        console.log(DisplayStudents());
    }
    else if(choice===2){
        let sid=prompt("Enter Student ID:")
        console.log(search(sid));
    }
    else if(choice===3){
        let stuid=prompt("Enter Student Id:");
        let companyname=prompt("Enter Company Name:")
        console.log(check_eligibility(stuid,companyname));
    }
    else if(choice===4){
        console.log(placedstudents());
    }
    else if(choice===5){
        console.log(notplacedstudents());
    }
    else if(choice===6){
        console.log(deparment_statistics());
    }
    else if(choice===7){
         console.log(placement_statistics());
    }
    else if(choice===8){
        let studentid=prompt("Enter Student ID:");
        let company=prompt("Enter Company:");
        let package=prompt("Enter Package:");
        update_placement(studentid,company,package);
    }
    else if(choice===9){
        let comapany_name=prompt("Enter a company name:")
        company_statistics(comapany_name);
    }
    else if(choice===10){
        highest_package();
    }
    else if(choice===11){
        let skill=prompt("Enter the Skill:");
        search_skill(skill);
    }
    else if(choice===12){
        let minCGPA=prompt("Enter a minimum CGPA:");
        above_CGPA(minCGPA);
    }
    else if(choice===0){
        break;
        }
    }
    