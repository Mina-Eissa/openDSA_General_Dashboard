import SelectMenu from '../Components/SelectMenu'

function home() {
  return (
    <>
      <SelectMenu />
      <div className="h-screen flex justify-start items-start p-4">
        <div className="text-4xl font-bold">My Home Page</div>
      </div>
    </>
  );
}

export default home;
